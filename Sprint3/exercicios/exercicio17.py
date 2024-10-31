def dividirLista(list):
    tamanho = len(list)
    lista1 = list[:4]
    lista2 =list[4:8]
    lista3 = list[8:]
    print(f'{lista1} {lista2} {lista3}')



lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

dividirLista(lista)