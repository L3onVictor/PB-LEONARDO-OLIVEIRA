import csv
import requests
import json
import pandas as pd

# Configurações da API TMDB
api_key = "7ac33345c0f52862959af97e38df7616"
search_url = "https://api.themoviedb.org/3/search/movie"
details_url = "https://api.themoviedb.org/3/movie"
credits_url = "https://api.themoviedb.org/3/movie/{}/credits"

# Função para buscar informações do TMDB pelo título original
def buscar_dados_tmdb(titulo_original):
    print(f"Buscando: {titulo_original}")
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

# Função para obter detalhes adicionais de um filme no TMDB
def obter_detalhes_tmdb(movie_id):
    response = requests.get(f"{details_url}/{movie_id}", params={"api_key": api_key, "language": "pt-BR"})
    if response.status_code == 200:
        return response.json()
    return None

# Função para obter os créditos (atores e diretor) de um filme no TMDB
def obter_creditos_tmdb(movie_id):
    response = requests.get(f"{credits_url.format(movie_id)}", params={"api_key": api_key, "language": "pt-BR"})
    if response.status_code == 200:
        return response.json()
    return None

# Função para ler o arquivo CSV, filtrar os filmes com nota maior que 7 e selecionar comédia e animação
def ler_csv_filtrado(arquivo_csv):
    df = pd.read_csv(arquivo_csv, delimiter='|', encoding="utf-8")
    
    # Limpar dados ausentes ou inválidos
    df = df[df['genero'].notna() & (df['genero'] != '\\N')]  # Filtra linhas com gênero válido
    
    # Remover filmes duplicados com base no ID
    df = df.drop_duplicates(subset='id')  # Garante que cada filme seja único
    
    # Filtrar apenas os filmes de Comedy ou Animation e com nota média maior que 7
    df_filtrado = df[df['genero'].str.contains("Comedy|Animation", case=False, na=False)]
    df_filtrado = df_filtrado[df_filtrado['notaMedia'] > 7]  # Filtra por nota maior que 7
    
    return df_filtrado

# Função para processar filmes e obter informações adicionais do TMDB
def processar_filmes(filmes_df):
    filmes_comedia = []
    filmes_animated = []

    # Filtrar filmes de comédia e animação
    filmes_comedia_df = filmes_df[filmes_df['genero'].str.contains("Comedy", case=False, na=False)]
    filmes_animated_df = filmes_df[filmes_df['genero'].str.contains("Animation", case=False, na=False)]

    # Selecionar os 20 filmes com maior número de votos de cada gênero
    filmes_comedia_top20 = filmes_comedia_df.nlargest(20, 'numeroVotos')
    filmes_animated_top20 = filmes_animated_df.nlargest(20, 'numeroVotos')

    # Agora, realizar as aquisições à API TMDB
    for index, filme in filmes_comedia_top20.iterrows():
        titulo_original = filme["tituloOriginal"]
        dados_tmdb = buscar_dados_tmdb(titulo_original)
        
        if dados_tmdb:
            # Obter gêneros e converter para os nomes dos gêneros
            generos = [genero["name"] for genero in dados_tmdb.get("genres", [])]
            
            # Obter detalhes adicionais do filme
            detalhes = obter_detalhes_tmdb(dados_tmdb["id"])
            if detalhes:
                # Obter os créditos (atores e diretor)
                creditos = obter_creditos_tmdb(dados_tmdb["id"])
                diretor = ""
                principais_atores = []
                
                if creditos:
                    # Obter o nome do diretor
                    for crew_member in creditos.get("crew", []):
                        if crew_member["job"] == "Director":
                            diretor = crew_member["name"]
                            break
                    
                    # Obter os 3 principais atores
                    for cast_member in creditos.get("cast", [])[:3]:
                        principais_atores.append(cast_member["name"])
                
                # Obter os países de produção
                paises = [pais["name"] for pais in detalhes.get("production_countries", [])]
                
                filme_completo = {
                    "id_csv": filme["id"],
                    "tituloPincipal": filme["tituloPincipal"],
                    "anoLancamento": filme["anoLancamento"],
                    "tmdb_id": detalhes["id"],
                    "titulo_tmdb": detalhes.get("title"),
                    "sinopse": detalhes.get("overview"),
                    "popularidade": detalhes.get("popularity"),
                    "nota_media": detalhes.get("vote_average"),
                    "votos": detalhes.get("vote_count"),
                    "data_lancamento": detalhes.get("release_date"),
                    "generos": generos,  # Gêneros pelo nome
                    "idioma_original": detalhes.get("original_language", ""),
                    "faturamento": detalhes.get("revenue"),
                    "orcamento": detalhes.get("budget"),
                    "diretor": diretor,
                    "principais_atores": principais_atores,
                    "pais_producao": paises,  # País de produção
                }

                filmes_comedia.append(filme_completo)

    for index, filme in filmes_animated_top20.iterrows():
        titulo_original = filme["tituloOriginal"]
        dados_tmdb = buscar_dados_tmdb(titulo_original)
        
        if dados_tmdb:
            # Obter gêneros e converter para os nomes dos gêneros
            generos = [genero["name"] for genero in dados_tmdb.get("genres", [])]
            
            # Obter detalhes adicionais do filme
            detalhes = obter_detalhes_tmdb(dados_tmdb["id"])
            if detalhes:
                # Obter os créditos (atores e diretor)
                creditos = obter_creditos_tmdb(dados_tmdb["id"])
                diretor = ""
                principais_atores = []
                
                if creditos:
                    # Obter o nome do diretor
                    for crew_member in creditos.get("crew", []):
                        if crew_member["job"] == "Director":
                            diretor = crew_member["name"]
                            break
                    
                    # Obter os 3 principais atores
                    for cast_member in creditos.get("cast", [])[:3]:
                        principais_atores.append(cast_member["name"])
                
                # Obter os países de produção
                paises = [pais["name"] for pais in detalhes.get("production_countries", [])]
                
                filme_completo = {
                    "id_csv": filme["id"],
                    "tituloPincipal": filme["tituloPincipal"],
                    "anoLancamento": filme["anoLancamento"],
                    "tmdb_id": detalhes["id"],
                    "titulo_tmdb": detalhes.get("title"),
                    "sinopse": detalhes.get("overview"),
                    "popularidade": detalhes.get("popularity"),
                    "nota_media": detalhes.get("vote_average"),
                    "votos": detalhes.get("vote_count"),
                    "data_lancamento": detalhes.get("release_date"),
                    "generos": generos,  # Gêneros pelo nome
                    "idioma_original": detalhes.get("original_language", ""),
                    "faturamento": detalhes.get("revenue"),
                    "orcamento": detalhes.get("budget"),
                    "diretor": diretor,
                    "principais_atores": principais_atores,
                    "pais_producao": paises,  # País de produção
                }

                filmes_animated.append(filme_completo)

    return filmes_comedia, filmes_animated

# Caminho para o arquivo CSV
arquivo_csv = 'movies.csv'

# Ler e filtrar os filmes
df_filtrado = ler_csv_filtrado(arquivo_csv)

# Processar os filmes e obter as informações do TMDB
filmes_comedia, filmes_animated = processar_filmes(df_filtrado)

# Salvar resultados em um arquivo JSON
with open('filmes_comedia_animacao.json', 'w', encoding='utf-8') as f:
    json.dump({"comedia": filmes_comedia, "animacao": filmes_animated}, f, ensure_ascii=False, indent=4)
