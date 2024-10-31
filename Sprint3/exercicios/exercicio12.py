teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def my_map(list, f):
    novaLista=[]
    for i in list:
        novaLista.append(f(i))
    return novaLista
    
def potencia(n):
    return n ** 2

print(my_map(teste, potencia))