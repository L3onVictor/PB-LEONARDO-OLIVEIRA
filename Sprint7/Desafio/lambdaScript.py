import boto3
import csv
import requests
import json
import pandas as pd
from io import StringIO
from datetime import datetime

# Configuração da API TMDB
API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
TMDB_BASE_URL = "https://api.themoviedb.org/3"
SEARCH_URL = f"{TMDB_BASE_URL}/search/movie"
DETAILS_URL = f"{TMDB_BASE_URL}/movie"
CREDITS_URL = f"{TMDB_BASE_URL}/movie/{{}}/credits"

# Inicialização do cliente S3
s3 = boto3.client('s3')

# Função para buscar informações de um filme
def buscar_dados_tmdb(titulo_original):
    print(f"Buscando dados para: {titulo_original}")
    params = {
        "api_key": API_KEY,
        "language": "pt-BR",
        "query": titulo_original
    }
    response = requests.get(SEARCH_URL, params=params)
    if response.ok:
        resultados = response.json().get("results", [])
        return resultados[0] if resultados else None
    return None

# Função para obter detalhes do filme
def obter_detalhes_tmdb(movie_id):
    response = requests.get(f"{DETAILS_URL}/{movie_id}", params={"api_key": API_KEY, "language": "pt-BR"})
    return response.json() if response.ok else None

# Função para obter créditos do filme
def obter_creditos_tmdb(movie_id):
    response = requests.get(CREDITS_URL.format(movie_id), params={"api_key": API_KEY, "language": "pt-BR"})
    return response.json() if response.ok else None

# Função para ler e filtrar o CSV do S3
def ler_csv_filtrado(bucket_name, arquivo_csv):
    print(f"Lendo arquivo {arquivo_csv} do bucket {bucket_name}")
    response = s3.get_object(Bucket=bucket_name, Key=arquivo_csv)
    content = response['Body'].read().decode('utf-8')
    df = pd.read_csv(StringIO(content), delimiter='|', encoding="utf-8")
    
    # Filtrando dados
    df = df[df['genero'].notna() & (df['genero'] != '\\N')].drop_duplicates(subset='id')
    return df[(df['genero'].str.contains("Comedy|Animation", case=False, na=False)) & (df['notaMedia'] > 7)]

# Função para processar filmes e enriquecer os dados com informações do TMDB
def processar_filmes(filmes_df):
    filmes_processados = {"comedia": [], "animacao": []}
    
    for genero, chave in [("Comedy", "comedia"), ("Animation", "animacao")]:
        filmes_top20 = filmes_df[filmes_df['genero'].str.contains(genero, case=False, na=False)].nlargest(20, 'numeroVotos')
        
        for _, filme in filmes_top20.iterrows():
            dados_tmdb = buscar_dados_tmdb(filme["tituloOriginal"])
            if not dados_tmdb:
                continue
            
            detalhes = obter_detalhes_tmdb(dados_tmdb["id"])
            creditos = obter_creditos_tmdb(dados_tmdb["id"]) if detalhes else None
            
            filme_completo = {
                "id_csv": filme["id"],
                "tituloPincipal": filme["tituloPincipal"],
                "anoLancamento": filme["anoLancamento"],
                "tmdb_id": detalhes.get("id") if detalhes else None,
                "titulo_tmdb": detalhes.get("title") if detalhes else None,
                "sinopse": detalhes.get("overview") if detalhes else None,
                "popularidade": detalhes.get("popularity") if detalhes else None,
                "nota_media": detalhes.get("vote_average") if detalhes else None,
                "votos": detalhes.get("vote_count") if detalhes else None,
                "data_lancamento": detalhes.get("release_date") if detalhes else None,
                "generos": [genero["name"] for genero in dados_tmdb.get("genres", [])] if dados_tmdb else [],
                "diretor": next((membro["name"] for membro in creditos.get("crew", []) if membro["job"] == "Director"), "") if creditos else "",
                "principais_atores": [ator["name"] for ator in (creditos.get("cast", [])[:3] if creditos else [])],
                "pais_producao": [pais["name"] for pais in (detalhes.get("production_countries", []) if detalhes else [])],
                "orcamento": detalhes.get("budget") if detalhes else None,
                "faturamento": detalhes.get("revenue") if detalhes else None,
            }
            filmes_processados[chave].append(filme_completo)
    
    return filmes_processados

# Função principal (Lambda Handler)
def lambda_handler(event, context):
    bucket_name = 'data-lake-do-leonardo'
    arquivo_csv = 'Raw/Local/CSV/Movies/2024/12/17/movies.csv'
    print("Iniciando processamento...")

    # Processando o CSV
    df_filtrado = ler_csv_filtrado(bucket_name, arquivo_csv)
    filmes_enriquecidos = processar_filmes(df_filtrado)
    
    # Gravando os resultados no S3
    data_atual = datetime.now().strftime('%Y/%m/%d')
    arquivo_json = f'Raw/TMDB/JSON/{data_atual}/movies_comedia_animacao.json'
    s3.put_object(
        Bucket=bucket_name,
        Key=arquivo_json,
        Body=json.dumps(filmes_enriquecidos, ensure_ascii=False, indent=4),
        ContentType='application/json'
    )
    print(f"Arquivo JSON gerado com sucesso: {arquivo_json}")
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Arquivo JSON salvo em {arquivo_json}')
    }
