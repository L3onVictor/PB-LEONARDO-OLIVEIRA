# Desafio
O desafio foi dividido em 3 etapas, onde tivemos que criar imagens e containers de determinados arquivos/scripts

# Etapa 1
Baixar o arquivo **carguru.py** e criar uma imagem com o mesmo

**Arquivo carguru:**
```py
import random

carros = ['Chevrolet Agile','Chevrolet C-10','Chevrolet Camaro','Chevrolet Caravan','Chevrolet Celta','Chevrolet Chevette','Chevrolet Corsa','Chevrolet Covalt','Chevrolet D-20','Chevrolet Monza','Chevrolet Onix','Chevrolet Opala','Chevrolet Veraneio','Citroën C3','Fiat 147','Fiat Argo','Fiat Cronos','Fiat Mobi','Fiat Panorama','Ford Corcel','Ford Escort','Ford F-1000','Ford Ka','Ford Maverick','Honda City','Honda Fit','Hyundai Azera','Hyundai HB20','Hyundai IX-35','Hyundai Veloster','Peugeot 2008','Peugeot 206','Peugeot 208','Peugeot 3008','Peugeot 306','Peugeot 308','Renault Kwid','Renault Logan','Renault Sandero','Renault Twingo','Renault Zoe','Toyota Etios','Toyota Yaris ','Volkswagen Apolo','Volkswagen Bora','Volkswagen Brasilia   ','Volkswagen Fusca','Volkswagen Gol','Volkswagen Kombi','Volkswagen Parati','Volkswagen Passat','Volkswagen Polo','Volkswagen SP2','Volkswagen Santana','Volkswagen Voyage','Volkswagen up!']

random_carros = random.choice(carros)

print('Você deve dirigir um '+ random_carros)


```

Código de criação de imagem:
```docker
FROM python:3

WORKDIR /carguru

COPY carguru.py .

CMD ["python", "carguru.py"]
```

Esse é um script do Dockerfile do diretório Carguru que criará a imagem do arquivo carguru.py. Apos a sua criação com o comando ```Docker build -t carguru_image .``` , devemos rodar essa imagem tm um container. Para fazermos isso utilizamos o comando: ```Docker run -it carguru_image``` que criará o container e imprimira um carro aleatório da lista do arquivo [carguru.py](Carguru/carguru.py).

Exemplo de saída possivel: 

```Você deve dirigir um Chevrolet Camaro``` 

# Etapa 2 
### É possível reutilizar o container?
Sim! É possível reutilizarmos o container anterior. Usando o comando Docker start -i \<Nome-do-container> Iremos conseguir usar o container novamente

Com o comando 

```docker
Docker start -i carguru_container
```
Reutilizamos conforme a imagem abaixo:

![Container carguru](../evidencias/Carguru%20Docker.png)

A primeira linha: **Você deve dirigir um Chevrolet Veaneio** foi a linha gerada na criação do container, já a segunda: **Você deve dirigir um Volkswagen Kombi** foi gerado com o comando a cima citado.

# Etapa 3 
Aqui devemos criar um Script que receberá:
- Uma String via input
- Gerar uma hash da palavra com o sha-1
- imprimir a hash em tela usando o método hexdigest
- Retornar ao passo 1

Código do Script:
```py
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
```

Com isso criaremos uma imagem da mesma forma que foi realizada na etapa 1:

Criação de imagem No dockerfile:
```docker
FROM python:3

WORKDIR /scriptDesafio4

COPY script-mascara.py .

CMD ["python","script-mascara.py"]
```

Usando o comando ```Docker build . .``` A imagem será criada.

Usando o comando ```Docker run -it <Nome-da-imagem>``` Rodamos a imagem em um container.

```docker
Docker run -it mascara-dados
```

esse comando terá a saída assim:

![mascarar-dados](../evidencias/mascarar-dados%20Dcoker.png)

- Pedirá para que seja inserido uma palavra
- mostrará a palavra já mascarada com o sha-1
- e perguntará se deseja inserir alguma outra palavra.
- caso sim, ele pedirá para que insira a nova palavra
- caso não, ele encerrara o container.

Com isso o desafio foi realizado.