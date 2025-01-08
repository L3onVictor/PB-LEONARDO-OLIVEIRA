import boto3
import csv
import requests
import json
import pandas as pd
from io import StringIO
from datetime import datetime

# Definindo a chave da API TMDB e as URLs para os endpoints
api_key = "xxxxxxxxxxxxxxxxxxxxxxx"
search_url = "https://api.themoviedb.org/3/search/movie"
details_url = "https://api.themoviedb.org/3/movie"
credits_url = "https://api.themoviedb.org/3/movie/{}/credits"

# Cliente S3
s3 = boto3.client('s3')

# Função para buscar informações de um filme pelo título original
def buscar_dados_tmdb(titulo_original):
    print(f"Procurando informações sobre: {titulo_original}")
    params = {
        "api_key": api_key,
        "language": "pt-BR",
        "query": titulo_original
    }
    response = requests.get(search_url, params=params)
    if response.status_code == 200:
        resultados = response.json().get("results", [])
        if resultados:
            return resultados[0]
    return None

# Função para obter os detalhes de um filme pelo ID
def obter_detalhes_tmdb(movie_id):
    response = requests.get(f"{details_url}/{movie_id}", params={"api_key": api_key, "language": "pt-BR"})
    if response.status_code == 200:
        return response.json()
    return None

# Função para obter informações sobre os créditos (atores e diretor) do filme
def obter_creditos_tmdb(movie_id):
    response = requests.get(f"{credits_url.format(movie_id)}", params={"api_key": api_key, "language": "pt-BR"})
    if response.status_code == 200:
        return response.json()
    return None

# Função para ler o arquivo CSV do S3
def ler_csv_filtrado(bucket_name, arquivo_csv):
    # Baixar o arquivo CSV do S3
    response = s3.get_object(Bucket=bucket_name, Key=arquivo_csv)
    content = response['Body'].read().decode('utf-8')
    
    # Ler o CSV
    df = pd.read_csv(StringIO(content), delimiter='|', encoding="utf-8")
    
    # Filtrar dados como no seu código original
    df = df[df['genero'].notna() & (df['genero'] != '\\N')]  
    df = df.drop_duplicates(subset='id')
    df_filtrado = df[df['genero'].str.contains("Comedy|Animation", case=False, na=False)]
    df_filtrado = df_filtrado[df_filtrado['notaMedia'] > 7]
    
    return df_filtrado

# Função para processar os filmes e adicionar informações do TMDB
def processar_filmes(filmes_df):
    filmes = []  # Lista única para armazenar todos os filmes

    # Separando filmes de comédia e animação
    filmes_comedia_df = filmes_df[filmes_df['genero'].str.contains("Comedy", case=False, na=False)]
    filmes_animated_df = filmes_df[filmes_df['genero'].str.contains("Animation", case=False, na=False)]

    # Top 20 de comédia e animação por número de votos
    filmes_comedia_top20 = filmes_comedia_df.nlargest(20, 'numeroVotos')
    filmes_animated_top20 = filmes_animated_df.nlargest(20, 'numeroVotos')

    # Processar filmes de comédia
    for index, filme in filmes_comedia_top20.iterrows():
        titulo_original = filme["tituloOriginal"]
        dados_tmdb = buscar_dados_tmdb(titulo_original)
        
        if dados_tmdb:
            generos = [genero["name"] for genero in dados_tmdb.get("genres", [])]
            generos.append("comedia")  # Adiciona "comedia" ao campo generos
            detalhes = obter_detalhes_tmdb(dados_tmdb["id"])
            
            if detalhes:
                creditos = obter_creditos_tmdb(dados_tmdb["id"])
                diretor = ""
                principais_atores = []
                
                if creditos:
                    for crew_member in creditos.get("crew", []):
                        if crew_member["job"] == "Director":
                            diretor = crew_member["name"]
                            break
                    
                    for cast_member in creditos.get("cast", [])[:3]:
                        principais_atores.append(cast_member["name"])
                
                paises = [pais["name"] for pais in detalhes.get("production_countries", [])]
                
                filme_completo = {
                    "id_csv": filme["id"],
                    "tituloPincipal": filme["tituloPincipal"],
                    "anoLancamento": filme["anoLancamento"],
                    "tmdb_id": detalhes["id"],
                    "titulo_tmdb": detalhes.get("title"),
                    "popularidade": detalhes.get("popularity"),
                    "nota_media": detalhes.get("vote_average"),
                    "votos": detalhes.get("vote_count"),
                    "data_lancamento": detalhes.get("release_date"),
                    "generos": generos,
                    "idioma_original": detalhes.get("original_language", ""),
                    "faturamento": detalhes.get("revenue"),
                    "orcamento": detalhes.get("budget"),
                    "diretor": diretor,
                    "principais_atores": principais_atores,
                    "pais_producao": paises,
                }
                filmes.append(filme_completo)

    # Processar filmes de animação (mesma lógica de comédia)
    for index, filme in filmes_animated_top20.iterrows():
        titulo_original = filme["tituloOriginal"]
        dados_tmdb = buscar_dados_tmdb(titulo_original)
        
        if dados_tmdb:
            generos = [genero["name"] for genero in dados_tmdb.get("genres", [])]
            generos.append("animacao")  # Adiciona "animacao" ao campo generos
            detalhes = obter_detalhes_tmdb(dados_tmdb["id"])
            
            if detalhes:
                creditos = obter_creditos_tmdb(dados_tmdb["id"])
                diretor = ""
                principais_atores = []
                
                if creditos:
                    for crew_member in creditos.get("crew", []):
                        if crew_member["job"] == "Director":
                            diretor = crew_member["name"]
                            break
                    
                    for cast_member in creditos.get("cast", [])[:3]:
                        principais_atores.append(cast_member["name"])
                
                paises = [pais["name"] for pais in detalhes.get("production_countries", [])]
                
                filme_completo = {
                    "id_csv": filme["id"],
                    "tituloPincipal": filme["tituloPincipal"],
                    "anoLancamento": filme["anoLancamento"],
                    "tmdb_id": detalhes["id"],
                    "titulo_tmdb": detalhes.get("title"),
                    "popularidade": detalhes.get("popularity"),
                    "nota_media": detalhes.get("vote_average"),
                    "votos": detalhes.get("vote_count"),
                    "data_lancamento": detalhes.get("release_date"),
                    "generos": generos,
                    "idioma_original": detalhes.get("original_language", ""),
                    "faturamento": detalhes.get("revenue"),
                    "orcamento": detalhes.get("budget"),
                    "diretor": diretor,
                    "principais_atores": principais_atores,
                    "pais_producao": paises,
                }
                filmes.append(filme_completo)

    return filmes  # Retorna a lista única com todos os filmes

# Função Lambda para processar e enviar os resultados
def lambda_handler(event, context):
    bucket_name = 'data-lake-do-leonardo'  # Substitua pelo nome do seu bucket S3
    arquivo_csv = 'Raw/Local/CSV/Movies/2024/12/17/movies.csv'
    
    # Ler e filtrar o CSV
    df_filtrado = ler_csv_filtrado(bucket_name, arquivo_csv)
    filmes = processar_filmes(df_filtrado)

    # Preparar o arquivo JSON
    data_atual = datetime.now().strftime('%Y/%m/%d')
    arquivo_json = f'Raw/TMDB/JSON/{data_atual}/movies_comedia_animacao.json'
    
    # Gravar o JSON de volta no S3
    s3.put_object(
        Bucket=bucket_name,
        Key=arquivo_json,
        Body=json.dumps(filmes, ensure_ascii=False, indent=4),
        ContentType='application/json'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Arquivo JSON gerado e enviado para: {arquivo_json}')
    }
