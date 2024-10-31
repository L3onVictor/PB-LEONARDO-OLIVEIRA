numeros = []
for i in range(4,7):
    numeros.append(i)
    if i %2 == 0:
        print(f'Par: {i}')
    else:
        print(f'Ímpar: {i}')