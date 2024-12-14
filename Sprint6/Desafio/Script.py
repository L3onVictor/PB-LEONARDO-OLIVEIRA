import boto3

# Cria a sessão usando o perfil especificado
session = boto3.Session(profile_name='207567778397_AdministratorAccess')

# Cria o cliente S3 a partir da sessão
s3_client = session.client('s3')

# Solicita o nome do bucket ao usuário
bucket_name = input("Digite o nome do bucket: ")

try:
    # Cria o bucket
    s3_client.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' criado com sucesso!")
except Exception as e:
    print(f"Erro ao criar o bucket: {e}")
