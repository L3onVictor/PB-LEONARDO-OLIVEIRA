with open('estudantes.csv', 'r', encoding='utf-8' ) as estudantes:
    alunos = []

    for i in estudantes:
        dados = i.strip().split(',')
        nome = dados[0]
        notas = list(map(int, dados[1:]))

        maiores_notas = sorted(notas, reverse=True)[:3]

        calculo_media = lambda x: round(sum(x) / len(x), 2)

        media = calculo_media(maiores_notas)

        alunos.append((nome, maiores_notas, media))

    alunos_order = sorted(alunos, key=lambda nome: nome[0])

for j in alunos_order:
    print(f'Nome: {j[0]} Notas: {j[1]} Média: {j[2]}')