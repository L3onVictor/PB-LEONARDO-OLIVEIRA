# Desafio
Esse desafio dará continuação ao desafio da Sprint anterior. Essa é a **etapa 3** da elaboração do Desafio final. Nessa etapa iremos adicionar os dados que estão na camada **Raw** para a camada **Trusted** por meio de um job no **AWS Glue**. Esse job deve enviar o arquivo **csv** bruto, que foi armazenado na **Sprint 6** e o arquivo **json** que fiu elaborado na **Sprint 7** e, posteriormente, acessar esses dados por meio do Amazon Athena.

> Camada Trusted: A camada Trusted de um data lake corresponde àquela em que os dados
encontram-se limpos e são confiáveis. É resultado da integração das diversas fontes de origem, que encontram-se na
camada anterior, que chamamos de Raw.
## Perguntas relacionadas a análise do banco de dados
1. Qual a média de custos dos filmes do gênero de comédia e animação.
2. Em qual década os filmes de aimação tiveram maior sucesso.
3. Em média, qual a diferença de faturamento entre os filmes desses 2 gêneros (Qual é mais lucrativo).
4. Quais atores são mais populares nos filmes de comédia.
5. Qual o gênero mais rentavel (com base no lucro e orçamento).
# Etapa 1 - Configurando e Executando um job no Glue

Primeiramenta iremos pesquisar pelo aws Glue

![glue](../Evidencias/pesquisando-glue.png)

Interface do AWS Glue

Para criar um job, devemos clicar no botão **Go to ETL jobs**

![interface glue](../Evidencias/dentro-glue.png)

Agora Iremos criar e configurar um Job

Clicando em Script editor, e em seguida escolhemos a engine que será utilizada, (No nosso caso, Spark)

![criando job](../Evidencias/criando-job01.png)

![criando job](../Evidencias/criando-job02.png)

Depois de criarmos um Job, iremos configura-lo.

Adicionamos um nome e mudamos algumas configurações conforme pedido no Desafio.

- **Work type**: informe G 1x

- **Requested number of workers**: Informe 2

- **Job timeout (minutes)**: Mantenha em 60 ou menos

![Configurando o job](../Evidencias/configurando-job.png)

Após a criação e configuração, daremos continuidade para desenvolver o Código que enviará o arquivo (nesse exemplo o arquivo json gerado na Sprint anterior) para a camada Trusted de um datalake.

![Script job json](../Evidencias/codigo-job-json.png)

Código que enviará o Arquivo json à camada Trusted:
```py
import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from datetime import datetime

# Inicializar o Spark
sc = SparkContext()
spark = SparkSession(sc)

# Configuração do Spark
spark.conf.set("spark.sql.files.ignoreCorruptFiles", "true")

# Definir o caminho do S3
caminho_s3 = "s3://data-lake-do-leonardo/Raw/TMDB/JSON/2025/01/07/movies_comedia_animacao.json"

# Definir a data de processamento (ano, mês, dia)
data_processamento = datetime.now()
ano = data_processamento.strftime('%Y')
mes = data_processamento.strftime('%m')
dia = data_processamento.strftime('%d')

# Definir o caminho de saída do arquivo Parquet
arquivo = f"s3://data-lake-do-leonardo/Raw/Trusted/TMDB/PARQUET/comedia_animacao/{ano}/{mes}/{dia}"

# Carregar o arquivo JSON
df = spark.read.option("multiline", "true").json(caminho_s3)

df.show()

# Transformar os dados para o formato Parquet e gravar no S3
df.write.parquet(arquivo, mode="overwrite")

print(f"Arquivo Parquet salvo em: {arquivo}")

```

Após criarmos o código, devemos salvar e rodar o mesmo

![rodando o job](../Evidencias/rodando-job.png)

Com isso percebemos que o job está sendo executado e esperamos a sua conclusão.

Antes do job ser concluido, nota-se que não há nenhuma camada Trusted no Bucket

![No trusted](../Evidencias/bucket-sem-trusted.png)

Apôs ser executado, podemos ver o caminho que foi criado no Bucket para a transferencia do arquivo .json.

> O caminho para qual o arquivo deve ser armazenado deve seguir a seguinte estrutura:

```Origem do dado\formato do dado\especificação do dado\data de processamento separada por ano\mes\dia\arquivo```

> Job concluido com sucesso

![job sucess](../Evidencias/job-concluido.png)

> Diretorio trusted criado depois do diretorio **Raw** 

![caminho trusted](../Evidencias/caminho-trusted.png)

> Origem do dado **TMDB**

![tmdb](../Evidencias/tmdb.png)

> Formato do dado **PARQUET**

![parquet](../Evidencias/parquet.png)

> Especificação do dado **comedia_animacao**

![comedia_animacao](../Evidencias/comedia_animacao.png)

> Ano

![ano](../Evidencias/ano.png)

> Mês

![mes](../Evidencias/mes.png)

> Dia

![dia](../Evidencias/dia.png)

Ao final desse caminho O arquivo .PARQUET estará armazenado

![arquivi](../Evidencias/arquivo-enviado.png)

# Etapa 2 - Criando um Crawler para visualização da tabela no Athena

Agora, usando o Glue Data Catalog, iremos criar um Crawler para visualizarmos as Tabelas dos arquivos enviados.

No canto Esquerdo da interface no Glue, clicamos em crawler e, em seguida, em create crawler

![criando crawler](../Evidencias/criando-crawler.png)

Agora iremos configurar o crawler

> Adicionamos o seu nome

![Configurando crawler](../Evidencias/configurando-crawler01.png)

> Em seguida o caminho do s3 que ele irá acessar.

![Configurando crawler](../Evidencias/configurando-crawler02.png)

> Nome da tabela e o local que ela será armazenada, no nosso caso, o local de armazenamento será o default

O nome da tabela será: **exemplo_tabela_athena_json**

![Configurando crawler](../Evidencias/configurando-crawler03.png)

Depois de configurado, o crawler será criado com sucesso, agora devemos o por em execução.

Clicando em **run crawler** ele será executado.

![crawler criado](../Evidencias/crawler-criado.png)

Com isso podemos ver que o crawler foi executado
![exe crawler](../Evidencias/exe-crawler.png)

# Etapa 3 - Visualizando a tabela no Amazon Athena

Nessa etapa, iremos visualizar a tabela que acabara de criar na etapa anterior.

Antes de tudo, iremos pesquisar pelo Amazon athena.

![athena](../Evidencias/pesquisando-athena.png)

Podemos ver que no lado esquerdo há uma tabela chamada **exemplo_tabela_athena_json**, é nela que iremos realizar as consultas.

![tabela json](../Evidencias/tabela-criada.png)

Com esse código iremos pegar todas as colunas da tabela especifica e mostrar as 10 primeiras linhas

![código sql athena json](../Evidencias/codigo-tabela-json.png)

O resultado da tabela está da seguinte maneira:

![resultado tabela json](../Evidencias/tabela-json.png)

# Etapa 4 - Job para enviar o arquivo .csv

Como mostrado em exemplos anteriores, iremos criar um job, e configura-lo, como mostrado na **etapa 1**

Agora Criaremos o código que enviará o arquivo **csv**

![job csv script](../Evidencias/codigo-job-csv.png)

Código:
```py
import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, split
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from datetime import datetime

# Inicializar o Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
glueContext = GlueContext(SparkContext.getOrCreate())

job_name = args["JOB_NAME"]

# Caminho do arquivo CSV no S3
caminho_csv = "s3://data-lake-do-leonardo/Raw/Local/CSV/Movies/2024/12/17/movies.csv"

# Obter a data atual para organizar o caminho de saída
data_atual = datetime.now()
ano = data_atual.strftime('%Y')
mes = data_atual.strftime('%m')
dia = data_atual.strftime('%d')

# Caminho de saída no formato Parquet
parquet_file = f"s3://data-lake-do-leonardo/Raw/Trusted/Local/PARQUET/Movies/{ano}/{mes}/{dia}"

# Lendo o arquivo CSV com Glue
df = spark.read.option("header", "true") \
               .option("delimiter", "|") \
               .option("inferSchema", "true") \
               .csv(caminho_csv)

df = df.withColumn("genero_filtro", explode(split(col("genero"), ",")))

# Filtrar apenas os filmes de comédia e animação
df_filtrado = df.filter((col("genero_filtro") == "Comedy") | (col("genero_filtro") == "Animation"))

# Remover duplicatas com base no ID do filme
df_unicos = df_filtrado.dropDuplicates(["id"])

# Reduzir para um único arquivo
df_unico_arquivo = df_unicos.coalesce(1)

# Exibir os dados filtrados
df_unico_arquivo.show()

# Gravando os dados em formato Parquet no bucket S3
df_unico_arquivo.write.mode("overwrite").parquet(parquet_file)

print(f"Processamento concluído. Arquivo Parquet único salvo em: {parquet_file}")

```

Com isso realizado, vamos rodar o job.

![rodando Script csv](../Evidencias/rodando-job-csv.png)

![job sucess](../Evidencias/job-sucess.png)

Agora voltando ao Bucket, vamos verificar o que mudou

> No diretorio Trusted foi criado a pasta **Local** que seria a origem do dado.

![local](../Evidencias/pasta-local.png)

> O tipo de dado **PARQUET**

![parquet](../Evidencias/csv-parquet.png)

> Especificações do dad**Movie**

![movies](../Evidencias/movies.png)

> Ano

![ano](../Evidencias/csv-ano.png)

> Mês

![mes](../Evidencias/csv-mes.png)

> Dia

![dia](../Evidencias/csv-dia.png)

E, ao findar desse caminho, o arquivo **.csv** estará armazenado

![csv para parquet](../Evidencias/arquivo-csv.png)

Agora devemos criar um crawler para visualizarmos a tabela desse arquivo no Athena, para isso repetimos as etapas anteriores.

Agora com o crawler criado vamos ao Athena 

Com esse código ele mostrara todas as colunas da tabela e mostrará as 10 primeiras linhas

![codigo tabela csv](../Evidencias/codigo-tabela-csv.png)

Resultado do código anterior

![resultado tabela csv](../Evidencias/tabela-csv.png)

Com isso o Desafio foi finalizado. todos os arquivos enviados seguem a mesma estrutura de caminho, que seria: ```Origem do dado\formato do dado\especificação do dado\data de processamento separada por ano\mes\dia\arquivo```.