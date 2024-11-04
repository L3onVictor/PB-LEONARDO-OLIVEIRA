# Sprint 3
Nessa Sprint foi abordado o curso de python, e conceitos de ETL (Extract-transform-load)

> **python:** Foi abordado os seus fundamentos, estrutura de controles, manipulação de arquivos, funções, pacotes e, também, programação orientada a objetos (POO), dentre outros.

# Evidências
### Essas evidências estão relacionadas ao ***Desafio***.
[clique aqui](desafio) para ver a pasta **Desafios** com mais detalhes.

# Exercícios
### Primeira parte do Exercício I
1.
> EX01 - Exercícios Parte 1:
Desenvolva um código em Python que crie variáveis para armazenar o nome e a idade de uma pessoa, juntamente com seus valores correspondentes. Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

Codigo:
```python
nome = 'Leo'
idade = 20
completa_100 = 100 - idade + 2024
print(completa_100)
```

[Arquivo exercicio 01](exercicios/exercicio01.py)

2.
>EX02 - Exercícios Parte 1:
Escreva um código Python que use a função range() para adicionar três números em uma lista(Esta lista deve chamar-se 'números')  e verificar se esses três números são pares ou ímpares. Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).



Importante: Aplique a função range() em seu código.

Código:
```python
numeros = []
for i in range(4,7):
    numeros.append(i)
    if i %2 == 0:
        print(f'Par: {i}')
    else:
        print(f'Ímpar: {i}')
```

[Arquivo exercicio 02](exercicios/exercicio02.py)

3.
>EX03 -Exercícios Parte 1
Escreva um código Python para imprimir os números pares de 0 até 20 (incluso).
>
>Importante: Aplique a função range() em seu código.

Código:
```python
for i in range(0,21,2):
    print(i)
```

[Arquivo exercicio 03](exercicios/exercicio03.py)

4.
>EX04 - Exercícios Parte 1
Escreva um código Python para imprimir todos os números primos entre 1 até 100. Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.
>
>Importante: Aplique a função range().

Código:
```python
for i in range(1,101):
    if i <= 1:
        continue
    primo = True
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            primo = False
    if primo:
        print(i)
```

[Arquivo exercicio 04](exercicios/exercicio04.py)

5.
>EX05 - Exercícios Parte 1
Escreva um código Python que declara 3 variáveis:
>
>dia, inicializada com valor 22
>
>mes, inicializada com valor 10 e
>
>ano, inicializada com valor 2022
>
>Como saída, você deverá imprimir a data correspondente, no formato a seguir dia/mes/ano.

Código:
```python
dia = 22
mes = 10
ano = 2022
print(f'{dia}/{mes}/{ano}')
```

[Arquivo exercicio 05](exercicios/exercicio05.py)


### Segunda parte do Exercício I
6.
>EX06 - Exercícios Parte 2
Considere as duas listas abaixo:
>
>a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
>
>b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
>
>Escreva um programa para avaliar o que ambas as listas têm em comum (sem repetições), imprimindo a lista de valores da interseção na saída padrão.
>
>Importante:  Esperamos que você utilize o construtor set() em seu código.

Código:
```python
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
conjunto = set()
for i in a:
    for j in b:
        if i == j and i not in conjunto:
            conjunto.add(i)

print(list(conjunto))
```

[Arquivo exercicio 06](exercicios/exercicio06.py)

7.
>EX07 - Exercícios Parte 2
Dada a seguinte lista:
>
>a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>
>Faça um programa que gere uma nova lista contendo apenas números ímpares. 

Código:
```python
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)
print(b)
```

[Arquivo exercicio 07](exercicios/exercicio07.py)

8.
>EX08 - Exercícios Parte 2
Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.
>
>Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
>
>É necessário que você imprima no console exatamente assim:
>
>A palavra: maça não é um palíndromo
>
>A palavra: arara é um palíndromo 
>A palavra: audio não é um palíndromo
 >
>A palavra: radio não é um palíndromo
 >
>A palavra: radar é um palíndromo
 >
>A palavra: moto não é um palíndromo

Código:
```python
palindromo = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
for a in palindromo:
    if a == a[::-1]:
        print(f'A palavra: {a} é um palíndromo')
    else:
        print(f'A palavra: {a} não é um palíndromo')
```

[Arquivo exercicio 08](exercicios/exercicio08.py)

9.
>EX09 - Exercícios Parte 2
Dada as listas a seguir:
>
>primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
>
>Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".
>
>Exemplo:
>
>0 - João Soares está com 19 anos

Código:
```python
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, (primeirosNomes, sobreNomes, idades) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f'{i} - {primeirosNomes} {sobreNomes} está com {idades} anos')
```

[Arquivo exercicio 09](exercicios/exercicio09.py)

10.
>EX10 - Exercícios Parte 2
Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.
>
>['abc', 'abc', 'abc', '123', 'abc', '123', '123']

Código:
```python
teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def duplicado(lista):
    lista2 = set()
    for i in lista:
        if i not in lista2:
            lista2.add(i)
    print(list(lista2))

duplicado(teste)
```

[Arquivo exercicio 10](exercicios/exercicio10.py)

11.
> EX11 - Exercícios Parte 2
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

Código:
```python
import json

with open('person.json') as arquivo:
    dados = json.load(arquivo)
    
    print(dados)
```

[Arquivo json](exercicios/person.json)

[Arquivo exercicio 11](exercicios/exercicio11.py)

12.
>EX12 - Exercícios Parte 2
Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.
>
>Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.

Código:
```python
teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def my_map(list, f):
    novaLista=[]
    for i in list:
        novaLista.append(f(i))
    return novaLista
    
def potencia(n):
    return n ** 2

print(my_map(teste, potencia))
```

[Arquivo exercicio 12](exercicios/exercicio12.py)

13.
>EX13 - Exercícios Parte 2
Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

Código:
```python
arquivo = open('arquivo_texto.txt')
dados = arquivo.read()
arquivo.close()
print(dados, end='')
```

[Arquivo de texto](exercicios/arquivo_texto.txt)

[Arquivo exercicio 13](exercicios/exercicio13.py)

14.
>EX14 - Exercícios Parte 2
Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.
>
>Teste sua função com os seguintes parâmetros:
>
>(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

Código:
```python
def valorParametro(*naoNomeado, **nomeado):
    for i in naoNomeado:
        print(i)
    for value in nomeado.values():
        print(f'{value}')


valorParametro(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
```

[Arquivo exercicio 14](exercicios/exercicio14.py)

15.
> EX15 - Exercícios Parte 2
Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
>
>liga(): muda o estado da lâmpada para ligada
>
>desliga(): muda o estado da lâmpada para desligada
>
>esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
>
>Para testar sua classe:
>
>Ligue a Lampada
>
>Imprima: A lâmpada está ligada? True
>
>Desligue a Lampada
>
>Imprima: A lâmpada ainda está ligada? False

Código:
```python
class Lampada:
    def __init__(self, ligada: bool):
        self.ligada = ligada

    def liga(self):
        self.ligada = True
    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada
    pass

lampada = Lampada(False)

lampada.liga()
print("A lâmpada está ligada?", lampada.esta_ligada())

lampada.desliga()
print("A lâmpada ainda está ligada?", lampada.esta_ligada())
```

[Arquivo exercicio 15](exercicios/exercicio15.py)

16.
>EX16 - Exercícios Parte 2
Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.
>
>A string deve ter valor  "1,3,4,6,10,76"

Código:
```python
def somaString(str):
    numero = str.split(',')

    soma = sum(int(i) for i in numero)

    return soma

string = "1,3,4,6,10,76"

print(somaString(string))
```

[Arquivo exercicio 16](exercicios/exercicio16.py)

17.
>EX17 - Exercícios Parte 2
Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo
>
>lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

Código:
```python
def dividirLista(list):
    tamanho = len(list)
    lista1 = list[:4]
    lista2 =list[4:8]
    lista3 = list[8:]
    print(f'{lista1} {lista2} {lista3}')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

dividirLista(lista)
```

[Arquivo exercicio 17](exercicios/exercicio17.py)

18.
>EX18 - Exercícios Parte 2
Dado o dicionário a seguir:
>
>speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
>
>Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.

Código:
```python
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
listaValor = set()
for i in speed:
    if speed[i] not in listaValor:
        listaValor.add(speed[i])
print(sorted(list(listaValor)))
```

[Arquivo exercicio 18](exercicios/exercicio18.py)

19.
>EX19 - Exercícios Parte 2
Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
>
>Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
>
>import random 
**amostra aleatoriamente 50 números do intervalo 0...500**
random_list = random.sample(range(500),50)
>
>Use as variáveis abaixo para representar cada operação matemática:
>
>- mediana
>
>- media
>
>- valor_minimo 
>
>- valor_maximo 
>
>Importante: Esperamos que você utilize as funções abaixo em seu código:
>
>- random
>
>- max
>
>- min
>
>- sum

Código:
```python
import random

random_list = random.sample(range(500), 50)

listaOrdernada = sorted(random_list)

quant = len(listaOrdernada)

if(quant %2 == 0):
    mediana = (listaOrdernada[quant // 2-1] + listaOrdernada[quant // 2]) / 2

else:
    mediana = listaOrdernada[quant // 2]

media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')
```

[Arquivo exercicio 19](exercicios/exercicio19.py)

20.
>**EX20 -** 
Exercícios Parte 2
Imprima a lista abaixo de trás para frente.
>
>a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89] 

Código:
```python
a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a.reverse()
print(a)
```

[Arquivo exercicio 20](exercicios/exercicio20.py)

21.
> EX21 - Exercícios Parte 1
Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som.
>
>Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir.
>
>Imprima no console exatamente assim:
>
>- Pato
>- Voando...
>- Pato emitindo som...
>- Quack Quack
>- pardal
>- Voando...
>- Pardal emitindo som...
>- Piu Piu

Código:
```python
class Passaro:
    def voar(self):
        print("Voando...")

    def emitir_som(self):
        return

class Pato(Passaro):
    def emitir_som(self):
        print("Pato emitindo som...")
        print("Quack Quack")

class Pardal(Passaro):
    def emitir_som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")

pato = Pato()
print("Pato")
pato.voar()
pato.emitir_som()

pardal = Pardal()
print("Pardal")
pardal.voar()
pardal.emitir_som()
```

[Arquivo exercicio 21](exercicios/exercicio21.py)

22.
>EX22 - Exercícios Parte 1
Crie uma classe chamada Pessoa, com um atributo privado chamado nome (declarado internamente na classe como __nome) e um atributo público de nome id.
>
>Adicione dois métodos à classe, sendo um para definir o valor de __nome e outro para retornar o valor do respectivo atributo.
>
>Lembre-se que o acesso ao atributo privado deve ocorrer somente através dos métodos definidos, nunca diretamente.  Você pode alcançar este comportamento através do recurso de properties do Python.
>
>Veja um exemplo de como seu atributo privado pode ser lido e escrito:
>- pessoa = Pessoa(0) 
>- pessoa.nome = 'Fulano De Tal'
>- print(pessoa.nome)

Código:
```python
class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome=None
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
pessoa = Pessoa(0) 
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
```

[Arquivo exercicio 22](exercicios/exercicio22.py)

23.
>EX23 - Exercícios Parte 1
Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).
>
>Utilize os valores abaixo para testar seu exercício:
> - x = 4 
>- y = 5
>
>imprima:
>- Somando: 4+5 = 9
>- Subtraindo: 4-5 = -1

Código:
```python
class Calculo:
    
    def soma(self, x,y):
        print('Somado:', x+y)
    def subtracao(self, x,y):
        print('Subtraindo:', x-y)

calculo = Calculo()

calculo.soma(4, 5)
calculo.subtracao(4, 5)
```

[Arquivo exercicio 23](exercicios/exercicio23.py)

24.
>EX24 - Exercícios Parte 1
Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos ordenacaoCrescente e ordenacaoDecrescente.
>
>Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como listaBaguncada a lista [3,4,2,1,5] e instancie um outro objeto, decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8].
>
>Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método ordenacaoDecrescente.
>
>Imprima o resultado da ordenação crescente e da ordenação decresce
>
>-[1, 2, 3, 4, 5] 
>-[9, 8, 7, 6]

Código:
```python
class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        lista = self.listaBaguncada
        lista.sort()
        return lista

    def ordenacaoDecrescente(self):
        lista = self.listaBaguncada
        lista.sort(reverse=True)
        return lista
        
crescente = Ordenadora([3,4,2,1,5])

decrescente = Ordenadora([9,7,6,8])

print(crescente.ordenacaoCrescente())

print(decrescente.ordenacaoDecrescente())
```

[Arquivo exercicio 24](exercicios/exercicio24.py)

25.
>EX25 - Exercícios Parte 1
Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.
>
>Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”.
>
>Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.
>
>Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:
>
>“O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é da cor “w”.
>
>Sendo x, y, z e w cada um dos atributos da classe “Avião”.
>
>Valores de entrada:
>
>- modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul
>
>- modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14 passageiros: Cor Azul
>
>- modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12 passageiros: Cor Azul

Código:
```python
class Aviao:
    cor = 'azul'
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        
    def toString(self):
        print(f'O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima}, capacidade para {self.capacidade} passageiros e é da cor {self.cor}.')

aviao1 = Aviao('BOIENG456', 1500, 400,)
aviao2 = Aviao("Embraer Praetor 600", 863, 14)
aviao3 = Aviao("Antonov An-2", 258, 12)

aviao1.toString()
aviao2.toString()
aviao3.toString()
```
[Arquivo exercicio 25](exercicios/exercicio25.py)

## Exercicio parte II ETL
### Tudo o que compete ao exercicio II está armazenado em um arquivo separado

[Exercicio parte II ETL](exercicios/ExercicioETL/exercicioETL.ipynb)

Nesse exercicio foi pedido para realizarmos alguns scripts e armazenalos em arquivos **.txt**. O Arquivo a cima descreve tudo o que foi realizado nesse exercício
# Certificados

![Certificado aws aspectos economicos](certificados/AWS%20Aspectos%20economicos%20da%20nuvem%20%20Certificate.jpg)

![badge aws aspector economicos](certificados/aws-partner-cloud-economics-essentials.png)