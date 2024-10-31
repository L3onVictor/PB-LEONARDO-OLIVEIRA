palindromo = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
for a in palindromo:
    if a == a[::-1]:
        print(f'A palavra: {a} é um palíndromo')
    else:
        print(f'A palavra: {a} não é um palíndromo')