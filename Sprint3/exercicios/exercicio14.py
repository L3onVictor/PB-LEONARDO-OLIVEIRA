def valorParametro(*naoNomeado, **nomeado):
    for i in naoNomeado:
        print(i)
    for value in nomeado.values():
        print(f'{value}')


valorParametro(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

