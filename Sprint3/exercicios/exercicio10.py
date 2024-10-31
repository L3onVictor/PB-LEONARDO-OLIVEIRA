teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def duplicado(lista):
    lista2 = set()
    for i in lista:
        if i not in lista2:
            lista2.add(i)
    print(list(lista2))

duplicado(teste)