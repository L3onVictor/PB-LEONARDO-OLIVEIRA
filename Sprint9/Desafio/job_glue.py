import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, explode, expr
import datetime

# Configurações do Glue Job
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Caminho do arquivo Parquet no S3
nomeBucket = "data-lake-do-leonardo"
bucket = f"s3://{nomeBucket}/Trusted/TMDB/PARQUET/comedia_animacao/2025/01/23/part-00000-fb266c25-5dc4-405c-9623-c4e14fd62f28-c000.snappy.parquet"

# Lendo o arquivo Parquet
df = spark.read.parquet(bucket)

# Criando DimFilmes
dim_filmes = df.selectExpr(
    "tmdb_id",
    "tituloPincipal AS titulo_original",
    "genero_principal"
).dropDuplicates()

# Criando DimDiretor
dim_diretor = df.selectExpr(
    "ROW_NUMBER() OVER (ORDER BY diretor) AS id_diretor",
    "diretor AS nome_diretor"
).dropDuplicates(["nome_diretor"])

# Criando DimAtores
dim_atores = df.select(explode("principais_atores").alias("nome_ator")) \
    .dropDuplicates() \
    .withColumn("id_ator", expr("ROW_NUMBER() OVER (ORDER BY nome_ator)"))

# Criando DimPais
dim_pais = df.select(explode("pais_producao").alias("nome_pais")) \
    .dropDuplicates() \
    .withColumn("id_pais", expr("ROW_NUMBER() OVER (ORDER BY nome_pais)"))

# Criando FatoFilme e explodindo as listas
df_exploded_pais_atores = df.withColumn("pais", explode(df["pais_producao"])) \
                            .withColumn("ator", explode(df["principais_atores"]))

# join com as tabelas de fato
fato_filme = df_exploded_pais_atores \
    .join(dim_diretor, df["diretor"] == dim_diretor["nome_diretor"], "left") \
    .join(dim_pais, df_exploded_pais_atores["pais"] == dim_pais["nome_pais"], "left") \
    .join(dim_atores, df_exploded_pais_atores["ator"] == dim_atores["nome_ator"], "left") \
    .withColumn("id_filme", expr("ROW_NUMBER() OVER (ORDER BY tmdb_id)")) \
    .selectExpr(
        "id_filme",
        "tmdb_id",
        "id_diretor",
        "anoLancamento AS ano_lancamento",
        "nota_media",
        "faturamento",
        "orcamento",
        "popularidade",
        "id_pais",
        "id_ator"
    )

# Obtendo a data atual
data_atual = datetime.datetime.now()
ano = data_atual.year
mes = data_atual.month
dia = data_atual.day

# Caminho de saída para dimensões e fato
diretorioDim = f"s3://{nomeBucket}/Refined/dim/PARQUET/{ano}/{mes:02d}/{dia:02d}/"
diretorioFato = f"s3://{nomeBucket}/Refined/fato/PARQUET/{ano}/{mes:02d}/{dia:02d}/"

# salvar no S3
def enviar_arquivo(df, table_name, output_path):
    df.write.mode("overwrite").parquet(f"{output_path}{table_name}.parquet")

# Enviar as tabelas para o bucket
enviar_arquivo(dim_filmes, "DimFilmes", diretorioDim)
enviar_arquivo(dim_diretor, "DimDiretor", diretorioDim)
enviar_arquivo(dim_atores, "DimAtores", diretorioDim)
enviar_arquivo(dim_pais, "DimPais", diretorioDim)

enviar_arquivo(fato_filme, "FatoFilme", diretorioFato)

job.commit()
