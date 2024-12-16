import boto3
import os
from datetime import datetime

# Cria a sessão usando o perfil especificado
session = boto3.Session(profile_name='207567778397_AdministratorAccess')

# Cria o cliente S3 a partir da sessão
s3_client = session.client('s3')

# Solicita o nome do bucket ao usuário
bucket_name = 'data-lake-do-leonardo'

try:
    # Cria o bucket
    s3_client.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' criado com sucesso!")
except Exception as e:
    print(f"Erro ao criar o bucket: {e}")


arquivo = '/app/Filmes+e+Series'

data = datetime.now()
ano = data.year
mes = f'{data.month:02d}'
dia = f'{data.day:02d}'

file_upload = {
    'movies.csv': f'Raw/Local/CSV/Movies/{ano}/{mes}/{dia}/movies.csv',
    'series.csv': f'Raw/Local/CSV/Series/{ano}/{mes}/{dia}/series.csv'
}


for local_file, s3_key in file_upload.items():
    file_path = os.path.join(arquivo, local_file)  # Caminho completo do arquivo no sistema
    if os.path.exists(file_path):
        try:
            # Faz o upload do arquivo
            s3_client.upload_file(file_path, bucket_name, s3_key)
            print(f"Arquivo '{local_file}' enviado com sucesso para '{s3_key}' no bucket '{bucket_name}'!")
        except Exception as e:
            print(f"Erro ao enviar o arquivo '{local_file}': {e}")
    else:
        print(f"Arquivo '{local_file}' não encontrado no diretório '{arquivo}'.")