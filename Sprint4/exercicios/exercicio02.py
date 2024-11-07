def conta_vogais(texto:str)-> int:
    vogais = ['a', 'e', 'i','o','u']
    lista = list(filter(lambda x: x.lower() in vogais, texto))
    
    count = len(lista)
    
    return count