def somaString(str):
    numero = str.split(',')

    soma = sum(int(i) for i in numero)

    return soma

string = "1,3,4,6,10,76"

print(somaString(string))