import csv
import requests
import json
import pandas as pd

# Definindo a chave da API TMDB e as URLs para os endpoints
api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
search_url = "https://api.themoviedb.org/3/search/movie"
details_url = "https://api.themoviedb.org/3/movie"
credits_url = "https://api.themoviedb.org/3/movie/{}/credits"

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

# Função para ler o arquivo CSV e filtrar filmes de comédia e animação com nota maior que 7
def ler_csv_filtrado(arquivo_csv):
    df = pd.read_csv(arquivo_csv, delimiter='|', encoding="utf-8")
    df = df[df['genero'].notna() & (df['genero'] != '\\N')]  # Remover linhas inválidas
    df = df.drop_duplicates(subset='id')  # Garantir que cada filme seja único
    df_filtrado = df[df['genero'].str.contains("Comedy|Animation", case=False, na=False)]
    return df_filtrado[df_filtrado['notaMedia'] > 7]

# Função para processar filmes e adicionar informações do TMDB
def processar_filmes(filmes_df):
    filmes = []  # Lista única para armazenar todos os filmes
    
    # Processar filmes por gênero
    for genero, filtro in [("comedia", "Comedy"), ("animacao", "Animation")]:
        filmes_genero_df = filmes_df[filmes_df['genero'].str.contains(filtro, case=False, na=False)]
        filmes_top20 = filmes_genero_df.nlargest(20, 'numeroVotos')
        
        for index, filme in filmes_top20.iterrows():
            titulo_original = filme["tituloOriginal"]
            dados_tmdb = buscar_dados_tmdb(titulo_original)
            
            if dados_tmdb:
                generos = [g["name"] for g in dados_tmdb.get("genres", [])]
                generos.append(genero)  # Adiciona o gênero correspondente
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
                        "genero": genero,  # Campo específico do gênero
                    }
                    filmes.append(filme_completo)
    return filmes

# Caminho para o arquivo CSV
arquivo_csv = 'movies.csv'

# Filtrando e processando os filmes
df_filtrado = ler_csv_filtrado(arquivo_csv)
filmes = processar_filmes(df_filtrado)

# Salvando os resultados em um único arquivo JSON
with open('filmes.json', 'w', encoding='utf-8') as f:
    json.dump(filmes, f, ensure_ascii=False, indent=4)
