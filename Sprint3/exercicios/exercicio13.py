arquivo = open('arquivo_texto.txt')
dados = arquivo.read()
arquivo.close()
print(dados, end='')