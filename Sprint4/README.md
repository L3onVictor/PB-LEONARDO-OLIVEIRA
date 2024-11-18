# Sprint 4
Nessa Sprint foi abordado o Docker, que é uma ferramenta de criação e gerenciamento de containers. Além do Curso da AWS credenciamento técnico e fundamentos técnicos.

***Nesses cursos foram abordados:***

> **AWS Partner - Credenciamento Técnico:** 
>
> - Descrever a presença global da AWS e como ela afeta as implantações dos clientes.
> - Identificar os principais serviços da AWS e relacioná-los a arquiteturas e casos de uso comuns.
> - Explicar os principais resultados do AWS Cloud Adoption Framework (AWS CAF) no que se refere à jornada do cliente.
> - Identificar estratégias de migração comuns que sejam mais relevantes para as necessidades de carga de trabalho de uma aplicação.
> - Descrever como usar o Well-Architected Framework para revisar a arquitetura do seu cliente.

> **AWS Partner - Fundamentos Técnicos:**
>
>- Descrever a terminologia e os conceitos relacionados aos produtos da AWS. 
>- Navegar no Console de Gerenciamento da AWS.
>- Apresentar os conceitos-chave das medidas de segurança da AWS e do AWS Identity and Access Management (IAM).
>- Diferenciar vários serviços computacionais da AWS, incluindo Amazon Elastic Compute Cloud (Amazon EC2), AWS Lambda, Amazon Elastic Container Service (Amazon ECS) e Amazon Elastic Kubernetes Service (Amazon EKS).
>- Compreender as ofertas de banco de dados e armazenamento da AWS, incluindo Amazon Relational Database Service (Amazon RDS), Amazon DynamoDB e Amazon Simple Storage Service (Amazon S3)
>- Conhecer os serviços de rede da AWS.
>- Acessar e configurar os recursos de monitoramento do Amazon CloudWatch.

> **Docker:**
>
>- Fluxos com os containers;
>- Criação e atualização de imagens;
>- Disponibilização de imagens no Docker Hub;
>- Criação e utilização de Volumes;
>- Bind Mount;
>- Criação e disponibilização de Networks;
>- Conexão externa, entre máquina host e entre containers do Docker;
>- Docker Compose para gerenciamento de múltiplos containers;
>- Criação de vários projetos práticos de diferentes tecnologias e etc.

# Evidências
As evidências estão relacionadas a pasta desafio.

[Clique aqui](Desafio/) Para vê a pasta desafios com mais atenção.

A maior parte das evidencias foram códigos e estão na pasta do desafio.

Container carguru

![carguru](evidencias/Carguru%20Docker.png)

Container mascarar-dados 

![mascarar dados](evidencias/mascarar-dados%20Dcoker.png)

# Exerciicos

1. 
> **E01:**
>Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
>
>Você deverá aplicar as seguintes funções no exercício:
>
>- map
>
>- filter
>
>- sorted
>
>- sum
>
>Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
>
>- a lista dos 5 maiores números pares em ordem decrescente;
>
>- a soma destes valores.

Código: 
```py
with open('number.txt') as num:
    numeros = num.read().splitlines()
    
numerosList = map(int, numeros)
    
par = list(filter(lambda x: x%2==0, numerosList))

order_par = sorted(par, reverse=True)[:5]

soma = sum(order_par)

print(order_par)

print(soma)
```

[Arquivo Ex1](exercicios/exercicio01.py)

2. 
>**E02:**
>Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.
>
>É obrigatório aplicar as seguintes funções:
>
>- len
>
>- filter
>
>- lambda
>
>Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.


Código: 
```py
def conta_vogais(texto:str)-> int:
    vogais = ['a', 'e', 'i','o','u']
    lista = list(filter(lambda x: x.lower() in vogais, texto))
    
    count = len(lista)
    
    return count
```

[Arquivo Ex2](exercicios/exercicio02.py)

3. 
>**E03:**
>A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 
>
>Abaixo apresentando uma possível entrada para a função.
```py
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
    ]
```

>A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. Na lista anterior, por exemplo, teríamos como resultado final 200.
>
>Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:
>
>- reduce (módulo functools)
>
>- map

Código: 
```py
from functools import reduce

def calcula_saldo(lancamentos) -> float:

    valor = map(lambda x: -x[0] if x[1] == 'D' else x[0], lancamentos)
    
    resultado = reduce(lambda x, y: x + y, valor)
    
    return resultado

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

print(calcula_saldo(lancamentos))
```

[Arquivo Ex3](exercicios/exercicio03.py)

4. 
> **E04:**
A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.
>
>Veja o exemplo:
>
>Entrada
>
```py
operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
```
>Aplicar as operações aos pares de operandos

 ```py 
[ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ]
``` 
>
>Obter o maior dos valores
>
>- ```12```
>
>Na resolução da atividade você deverá aplicar as seguintes funções:
>
>- max
>
>- zip
>
>- map

Código: 
```py
def calcular_valor_maximo(operadores,operandos) -> float:
    resultado = map(
        lambda valor: valor[1][0] + valor[1][1] if valor[0] == '+' 
        else valor[1][0] - valor[1][1] if valor[0] == '-' 
        else valor[1][0] * valor[1][1] if valor[0] == '*' 
        else valor[1][0] / valor[1][1] if valor[0] == '/' 
        else valor[1][0] % valor[1][1] if valor[0] == '%' 
        else None,
        zip(operadores, operandos)
    )
    
    return max(resultado)
    
operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

print(calcular_valor_maximo(operadores, operandos))
```
[Arquivo Ex4](exercicios/exercicio04.py)

5. 
>**E05:**
>Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo ```[0-10]```. É o arquivo estudantes.csv de seu exercício.
>
>Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:
>
>Nome do estudante
>
>Três maiores notas, em ordem decrescente
>
>Média das três maiores notas, com duas casas decimais de precisão
>
>O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:
```python
Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>
```
>Exemplo:
>
>Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
>
>Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33
>
>Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:
>
>- round
>
>- map
>
>- sorted

Código: 
```py
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
```

[Arquivo Ex5](exercicios/exercicio05.py)

6. 
>**E06:**
>Você foi encarregado de desenvolver uma nova feature  para um sistema de gestão de supermercados. O analista responsável descreveu o requisito funcional da seguinte forma:
>
>- Para realizar um cálculo de custo, o sistema deverá permitir filtrar um determinado conjunto de produtos, de modo que apenas aqueles cujo valor unitário for superior à média deverão estar presentes no resultado. Vejamos o exemplo:
>
>Conjunto de produtos (entrada):
>
>- Arroz: 4.99
>
>- Feijão: 3.49
>
>- Macarrão: 2.99
>
>- Leite: 3.29
>
>- Pão: 1.99
>
>Produtos com valor acima da média:
>
>- Arroz: 4.99
>
>- Feijão: 3.49
>
>Observe que estamos definindo a assinatura de uma função como parte de sua resposta. Você não pode mudá-la, apenas codificar seu corpo. O parâmetro conteudo é um dicionário cuja chave contém o nome do produto e o valor, o respectivo preço (ponto flutuante).
>
>Observe um exemplo de valor para conteudo:
```py
{
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}
```
> O retorno da função obrigatoriamente deve ser uma lista. Cada elemento da lista é uma tupla em que a primeira posição contém o nome do produto e a segunda, o respectivo preço. Veja um exemplo de retorno:
```py
[
 
('feijão', 3.49),
 
 ('arroz', 4.99)
 
]
```

> Importante: O retorno da função deve estar ordenado pelo preço do item (ordem crescente).

Código: 
```py
def maiores_que_media(conteudo:dict)->list:
    
    media = sum(conteudo.values()) / len(conteudo)

    conteudoList = [(key, value) for key, value in conteudo.items() if value > media]

    conteudoList_order = sorted(conteudoList, key=lambda value: value[1])

    return conteudoList_order

content = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

print(maiores_que_media(content))
```

[Arquivo Ex6](exercicios/exercicio06.py)

7.
>**E07:**
Generators são poderosos recursos da linguagem Python. Neste exercício, você deverá criar o corpo de uma função, cuja assinatura já consta em seu arquivo de início (def pares_ate(n:int):) .
>
>O objetivo da função pares_ate é retornar um generator para os valores pares no intervalo [2,n] . Observe que n representa o valor do parâmetro informado na chamada da função. 


Código: 
```py
def pares_ate(n: int):
    for i in range(2, n+1, 2):
        yield i

print(list(pares_ate(7)))
```

[Arquivo Ex7](exercicios/exercicio07.py)

# Certificados 
![AWS credenciamento tecnico](certificados/AWS%20crendencial%20(tecnico).jpg)


![AWS Fundamentos tecnicos](certificados/AWS-Fundamentos%20tecnicos.jpg)

![Badge](certificados/aws-partner-technical-accredited.png)