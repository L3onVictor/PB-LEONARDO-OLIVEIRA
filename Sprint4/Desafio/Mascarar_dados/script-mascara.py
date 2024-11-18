# Imposta o sha1 da Biblioteca hashlib
from hashlib import sha1

# Faz um laço de repetição
while True:
    # Recebe a palavra por um input
    palavra = str(input("Digite a palavra que será mascaraada: "))

    # mascara usando o sha1 e imprime com o hexdigest
    palavra_hash = sha1(palavra.encode()).hexdigest()
    
    # Printa a palavra já mascarada
    print(f"A palavra com a mascara é: {palavra_hash}")

    # Pergunta para encerrar o laço de repetição
    cond = str(input("Deseja inserir outra palavra? [Y/n]")).upper()

    # Se a resposta for 'N' (não) O laço de repetição é cancelado
    if cond == 'N':
        print("Saindo...")
        break
