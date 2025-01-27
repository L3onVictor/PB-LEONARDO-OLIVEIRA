import csv
import requests
import json
import pandas as pd

# Definindo a chave da API TMDB e as URLs para os endpoints
api_key = "7ac33345c0f52862959af97e38df7616"
search_url = "https://api.themoviedb.org/3/search/movie"
details_url = "https://api.themoviedb.org/3/movie"
credits_url = "https://api.themoviedb.org/3/movie/{}/credits"

# Função para buscar informações de um filme pelo título original
def buscar_dados_tmdb(titulo_original, tentativas=3):
    print(f"Procurando informações sobre: {titulo_original}")
    params = {
        "api_key": api_key,
        "language": "pt-BR",
        "query": titulo_original
    }
    for tentativa in range(tentativas):
        try:
            response = requests.get(search_url, params=params, timeout=10)
            if response.status_code == 200:
                resultados = response.json().get("results", [])
                if resultados:
                    return resultados[0]
            else:
                print(f"Erro na API TMDB: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Tentativa {tentativa + 1} falhou: {e}")
    return None


# Função para obter os detalhes de um filme pelo ID
def obter_detalhes_tmdb(movie_id, tentativas=3):
    for tentativa in range(tentativas):
        try:
            response = requests.get(f"{details_url}/{movie_id}", params={"api_key": api_key, "language": "pt-BR"}, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Erro na API TMDB (detalhes): {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Tentativa {tentativa + 1} falhou: {e}")
    return None


# Função para obter informações sobre os créditos (atores e diretor) do filme
def obter_creditos_tmdb(movie_id, tentativas=3):
    for tentativa in range(tentativas):
        try:
            response = requests.get(f"{credits_url.format(movie_id)}", params={"api_key": api_key, "language": "pt-BR"}, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Erro na API TMDB (créditos): {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Tentativa {tentativa + 1} falhou: {e}")
    return None


# Função para ler o arquivo CSV e filtrar filmes de comédia e animação com nota maior que 7
def ler_csv_filtrado(arquivo_csv):
    df = pd.read_csv(arquivo_csv, delimiter='|', encoding="utf-8")
    df = df[df['genero'].notna() & (df['genero'] != '\\N')]  # Remover linhas inválidas
    df = df.drop_duplicates(subset='id')  # Garantir que cada filme seja único
    df_filtrado = df[df['genero'].str.contains("Comedy|Animation", case=False, na=False)]
    return df_filtrado[df_filtrado['notaMedia'] > 7]

# Função para processar e limitar os filmes
def processar_filmes(filmes_df, limite_inicial=25, limite_final=15):
    filmes_processados = []
    
    # Selecionar os 25 primeiros filmes de comédia
    filmes_comedia = filmes_df[filmes_df['genero'].str.contains("Comedy", case=False, na=False)].nlargest(limite_inicial, 'numeroVotos')
    
    # Selecionar os 25 primeiros filmes de animação
    filmes_animacao = filmes_df[filmes_df['genero'].str.contains("Animation", case=False, na=False)].nlargest(limite_inicial, 'numeroVotos')
    
    # Unir os dois DataFrames e garantir unicidade
    filmes_selecionados = pd.concat([filmes_comedia, filmes_animacao]).drop_duplicates(subset="id")
    
    # Contadores de filmes por gênero
    comedia_contador, animacao_contador = 0, 0
    
    for _, filme in filmes_selecionados.iterrows():
        if comedia_contador >= limite_final and animacao_contador >= limite_final:
            break  # Já processou 20 de cada gênero
        
        titulo_original = filme["tituloOriginal"]
        dados_tmdb = buscar_dados_tmdb(titulo_original)
        
        # Apenas processe se houver correspondência exata
        if dados_tmdb:
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
                
                # Decisão correta do gênero principal
                if "Comedy" in filme["genero"] and "Animation" not in filme["genero"]:
                    genero = "comédia"
                elif "Animation" in filme["genero"] and "Comedy" not in filme["genero"]:
                    genero = "animação"
                else:
                    genero = "animação"  # Filmes que possuem ambos os gêneros são tratados como "animação"
                
                filme_completo = {
                    "id_csv": filme["id"],
                    "tituloPincipal": filme["tituloPincipal"],
                    "anoLancamento": filme["anoLancamento"],
                    "tmdb_id": detalhes["id"],
                    "titulo_tmdb": detalhes.get("title"),
                    "popularidade": detalhes.get("popularity"),
                    "nota_media": detalhes.get("vote_average"),
                    "votos": detalhes.get("vote_count"),
                    "generos": [g["name"] for g in detalhes.get("genres", [])],
                    "idioma_original": detalhes.get("original_language", ""),
                    "faturamento": detalhes.get("revenue"),
                    "orcamento": detalhes.get("budget"),
                    "diretor": diretor,
                    "principais_atores": principais_atores,
                    "pais_producao": paises,
                    "genero_principal": genero
                }
                
                # Adicionar ao gênero correto
                if genero == "comédia" and comedia_contador < limite_final:
                    filmes_processados.append(filme_completo)
                    comedia_contador += 1
                elif genero == "animação" and animacao_contador < limite_final:
                    filmes_processados.append(filme_completo)
                    animacao_contador += 1
    
    return filmes_processados


# Caminho para o arquivo CSV
arquivo_csv = 'movies.csv'

# Filtrar e processar os filmes
df_filtrado = ler_csv_filtrado(arquivo_csv)
filmes = processar_filmes(df_filtrado)

# Criar um DataFrame leve com os filmes processados
df_final = pd.DataFrame(filmes)

# Salvar os resultados no JSON
df_final.to_json('filmes.json', orient='records', force_ascii=False, indent=4)
