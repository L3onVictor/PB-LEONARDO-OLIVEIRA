# Sprint 5
Nessa Sprint foram vistos os fundamentos de Computação em Nuvem utilizando a Amazon Web Services, além do aws Cloud Quest

Cusros AWS:

> Cloud Practitioner: 
- Fundamentos da Computação em Nuvem
- Primeiros Passos na Nuvem
- Soluções de Computação
- Conceitos de Rede
- Bancos de Dados na Prática
- Conectar VPCs
- Primeiro Banco de Dados NoSQL
- Sistemas de Arquivos na Nuvem
- Aplicativos de Auto-Recuperação e Escalabilidade
- Aplicações Web Altamente Disponíveis
- Conceitos Principais de Segurança
- Economia de Nuvem

> Curso-padrão de preparação para o exame: AWS Certified Cloud Practitioner (CLF-C02 - Português):
- Conheça o exame AWS
- Conheça as questões no estilo do exame
- Conheça os tópicos do exame
- Prepare-se para o exame
    - Conceitos de nuvem
    - Segurança e conformidade
    - Tecnologia e serviços em nuvem
    - Cobrança, preços e suporte

# Evidências
### Essas evidências estão relacionadas ao ***Desafio*** e ***Exercicios***.
[clique aqui](desafio) para ver a pasta **Desafios** com mais detalhes.

Acessando S3
![Acessando S3](Evidencias/bucket.png)

Criando o bucket
![Criando bucket](Evidencias/criandoBucket.png)

Nomeando o Bucket
![Nome bucket](Evidencias/nomeandoBucket.png)

Finalizando a criação
![Finalizando bucket](Evidencias/execBucket.png)

Bucket criado
![Bucket criado](Evidencias/BucketCriado.png)

Bucket sem index inserido
![index not found](Evidencias/SemSite.png)

Criando uma hospedagem para o site estatico
![hospedagem site estatico](Evidencias/hospedandosite.png)

Noemando a hospedagem
![hospedagem nome](Evidencias/nomeandoSite.png)

Erro ao encontrar site
![error site](Evidencias/erroSite-privado.png)

Configurando a privacidade do site
![privaci config](Evidencias/configSiteStatico.png)

Acesso ao público bloqueado
![acesso bloqueado](Evidencias/bloquearAcesso.png) 

site privado
![site privado](Evidencias/siteprivado.png)

Deixando o site público
![site publico](Evidencias/SitePublico.png)

Site sem política de privacidade
![site sem politica](Evidencias/abaPolitica.png)

Adicionando uma política de privacidade ao site
![politica adicionada](Evidencias/editandoPolitica.png)

O bucket não possui arquivos index anexados (Não possui arquivos)
![sem arquivos](Evidencias/NoAQV.png)

Adicionando o **index** e o **error**
![index e error](Evidencias/movendoAqv.png)

Adicionando o arquivo .csv
![.csv](Evidencias/movendoArq2.png)

Finalização do site já rodando no bucket da aws
![Finalização do site](Evidencias/siteEstaticB.png)

Baixando arquivos csv no site demonstrado
![baixando csv](Evidencias/baixnadoCVS.png)

# Exercicios
Nesse exercicio foi pedido a criação de um bucket S3 para 

## ETAPA 1
### Criando um bucket na AWS

entrando na pagina **S3** da AWS

armazenar um site estático
![Acessando S3](Evidencias/bucket.png)

Criando o bucket
![Criando bucket](Evidencias/criandoBucket.png)

inserindo o nome no bucket e escolhendo a região us-east-1.
![Nome bucket](Evidencias/nomeandoBucket.png)

Finalizando a criação do bucket - ***Apertar em Criar Bucket***
![Finalizando bucket](Evidencias/execBucket.png)


Bucket Criado com sucesso
![Bucket criado](Evidencias/BucketCriado.png)

## ETAPA 2
### Habilitando a hospedagem de site estático
Ao clicarmos no bucket que foi criado anteriormente, podemos acessar suas configurações

Podemos ver que não há nenhum arquivo (Objeto) no bucket em questão
![index not found](Evidencias/SemSite.png)

Abrimos o submenu **Propriedades** e entramos em editar 
![hospedagem site estatico](Evidencias/hospedandosite.png)

Ao acessarmos, devemos colocar os nomes dos documentos de index e error e confirmamos e ativarmos a **Hospedagem de site estático**
![hospedagem nome](Evidencias/nomeandoSite.png)

Ao criarmos um site estático e lançarmos o seu link no navegador, um erro ocorrerá, pois o site estará privado
![error site](Evidencias/erroSite-privado.png)

Para resolvermos isso, devemos tornar o site público
## ETAPA 3
### editar as configurações do Bloqueio de acesso público

Para editarmos essa politica, devemos editar a aba **Bloquear acesso Público**
![acesso bloqueado](Evidencias/bloquearAcesso.png) 

E desmarcar todas as janelas 
![site privado](Evidencias/siteprivado.png)

Após isso, removermos as marcações e salvamos
![site sem politica](Evidencias/abaPolitica.png)

Agora com isso o site estará publico

## ETAPA 4
### Adicionar política de bucket que torna o conteúdo do bucket publicamente disponível

Agora iremos criar e atribuir uma política no Bucket

No submenu **Permissões** iremos até Política de Bucket
![site sem politica](Evidencias/abaPolitica.png)

e adicionaremos a seguinte Política e o salvamos
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::Bucket-Name/*"
            ]
        }
    ]
}
``` 

então ficará da seguinte maneira
![politica adicionada](Evidencias/editandoPolitica.png)

## ETAPA 5
### Configurar um documento de índice

Antes de tudo, lembras que o bucket ainda continua vazio.
![sem arquivos](Evidencias/NoAQV.png)

Aqui criaremos um arquivo chamado ***index.html*** que irá receber o site a ser hospedado. Nele estará o seguinte código:
```html
<html xmlns="http://www.w3.org/1999/xhtml" >
<head>
    <title>Home Page do meu WebSite - Tutorial de S3</title>
</head>
<body>
  <h1>Bem-vindo ao meu website</h1>
  <p>Agora hospedado em Amazon S3!</p>
  <a href="nome do arquivo CSV a ser baixado">Download CSV File</a> 
</body>
</html>
```

## ETAPA 6
### configurar documento de erros

Apos a criação desse arquivo, também criaremos um arquivo com o nome **error.html** e em sequencia faremos upload para o bucket
![index e error](Evidencias/movendoAqv.png)

Após adicionarmos os arquivos ao bucket, também adicionaremos um arquivo csv que foi nos entregue [nomes.csv](Exercicio/dados/nomes.csv)
![.csv](Evidencias/movendoArq2.png)

## ETAPA 7
### testar o endpoint do site

Após todas essas etapas, chegou a hora de testar o site rodando no bucket da aws. E esse foi o resuldadr 
![Finalização do site](Evidencias/siteEstaticB.png)

**Como pode ver, o site foi criado com sucesso e está funcionando normalmente**

Inclusive o botão de download é funcional e baixará os arquivos csv possivel
![baixando csv](Evidencias/baixnadoCVS.png)

**E com isso o exercicio foi finalizado**


# Certificados

![Cloud Quest](Certificados/aws-cloud-quest-cloud-practitioner.png)

[Link do bandge](https://www.credly.com/badges/847909e0-9ec9-472e-9ec0-a1c3ef367d60/public_url)

![aws certificate](Certificados/Curso-padrão%20de%20preparação%20para%20o%20exame%20AWS%20Certified%20Cloud%20Practitioner_page-0001.jpg)