def maiores_que_media(conteudo:dict)->list:
    
    media = sum(conteudo.values()) / len(conteudo)

    conteudoList = [(key, value) for key, value in conteudo.items() if value > media]

    conteudoList_order = sorted(conteudoList, key=lambda value: value[1])

    return conteudoList_order

content = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

print(maiores_que_media(content))