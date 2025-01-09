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
input_csv_path = "s3://data-lake-do-leonardo/Raw/Local/CSV/Movies/2024/12/17/movies.csv"

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
               .csv(input_csv_path)

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
