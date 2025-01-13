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
