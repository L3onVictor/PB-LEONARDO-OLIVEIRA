import requests
import json

# Chave de API e URLs base
api_key = "7ac33345c0f52862959af97e38df7616"
base_url = "https://api.themoviedb.org/3/discover/movie"
movie_details_url = "https://api.themoviedb.org/3/movie"

# Parâmetros para buscar filmes de comédia
params_comedia = {
    "api_key": api_key,
    "language": "pt-BR",
    "with_genres": "35",  # Código do gênero comédia
    "sort_by": "popularity.desc",
    "page": 1
}

# Parâmetros para buscar filmes de animação
params_animacao = {
    "api_key": api_key,
    "language": "pt-BR",
    "with_genres": "16",  # Código do gênero animação
    "sort_by": "popularity.desc",
    "page": 1
}

# Função para buscar até 25 filmes de um gênero
def get_filmes(params):
    filmes = []
    page = 1
    
    while len(filmes) < 25:  # Limita a 25 filmes no máximo
        params["page"] = page
        response = requests.get(base_url, params=params)
        
        if response.status_code != 200:
            print(f"Erro ao acessar API. Código: {response.status_code}")
            break

        data = response.json()
        filmes_pagina = data.get('results', [])
        filmes.extend(filmes_pagina)

        if len(filmes_pagina) == 0:  # Se não houver mais filmes, para
            break
        
        page += 1

    return filmes[:25]  # Garante que no máximo 25 filmes sejam retornados

# Obter filmes de comédia e animação
filmes_comedia = get_filmes(params_comedia)
filmes_animacao = get_filmes(params_animacao)

# Combina as duas listas
todos_filmes = filmes_comedia + filmes_animacao

print(f"Total de filmes encontrados: {len(todos_filmes)}")

# Detalhes completos dos filmes
filmes_completos = []
for filme in todos_filmes:
    movie_id = filme.get("id")
    detalhes_resposta = requests.get(f"{movie_details_url}/{movie_id}", params={"api_key": api_key, "language": "pt-BR"})
    
    if detalhes_resposta.status_code == 200:
        detalhes = detalhes_resposta.json()

        # Obter informações de elenco, equipe e faturamento
        creditos_resposta = requests.get(f"{movie_details_url}/{movie_id}/credits", params={"api_key": api_key, "language": "pt-BR"})
        diretor = "Não informado"
        atores_principais = []
        
        if creditos_resposta.status_code == 200:
            creditos = creditos_resposta.json()
            # Buscar diretor
            for pessoa in creditos.get("crew", []):
                if pessoa.get("job") == "Director":
                    diretor = pessoa.get("name")
                    break
            
            # Obter até 3 atores principais
            elenco = creditos.get("cast", [])
            atores_principais = [ator.get("name") for ator in elenco[:3]]

        # Adiciona informações de receita e orçamento
        receita = detalhes.get("revenue", 0)  # Faturamento em dólares
        orcamento = detalhes.get("budget", 0)  # Orçamento em dólares

        filme_completo = {
            "id": filme.get("id"),
            "titulo": filme.get("title"),
            "descricao": filme.get("overview"),
            "data_lancamento": filme.get("release_date"),
            "generos": filme.get("genre_ids"),
            "idioma_original": filme.get("original_language"),
            "popularidade": filme.get("popularity"),
            "nota_media": filme.get("vote_average"),
            "contagem_votos": filme.get("vote_count"),
            "diretor": diretor,
            "atores_principais": atores_principais,
            "orcamento": orcamento,
            "receita": receita
        }

        filmes_completos.append(filme_completo)
    else:
        print(f"Erro ao obter detalhes do filme ID {movie_id}")

# Salvar os filmes no arquivo JSON
output_file = "top25_filmes_comedia_animacao.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(filmes_completos, file, ensure_ascii=False, indent=4)

print(f"Dados salvos no arquivo '{output_file}'.")
