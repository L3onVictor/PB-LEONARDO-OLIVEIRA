import boto3
import os
from datetime import datetime

# Cria a sessão usando o perfil especificado
session = boto3.Session(profile_name='207567778397_AdministratorAccess')

# Cria o cliente S3 a partir da sessão
s3_client = session.client('s3')

# Nome do bucket
bucket_name = 'data-lake-do-leonardo'

# Caminho do arquivo no S3 e caminho onde o arquivo será salvo localmente
arquivo_s3 = 'Raw/TMDB/JSON/2025/01/14/movies_comedia_animacao.json'  # Caminho do arquivo no S3
arquivo_local = 'movies_comedia_animacao.json'  # Caminho onde o arquivo será salvo localmente

# Função para baixar o arquivo do S3
def baixar_arquivo_s3(bucket_name, arquivo_s3, arquivo_local):
    try:
        # Baixar o arquivo do S3
        s3_client.download_file(bucket_name, arquivo_s3, arquivo_local)
        print(f"Arquivo baixado com sucesso para: {arquivo_local}")
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")

# Chamada da função para baixar o arquivo
baixar_arquivo_s3(bucket_name, arquivo_s3, arquivo_local)
