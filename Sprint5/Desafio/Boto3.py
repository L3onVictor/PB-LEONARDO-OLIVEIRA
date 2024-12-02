import boto3
import pandas as pd

# Entra na seção do usuario e acessa o item s3
session = boto3.Session(profile_name='207567778397_AdministratorAccess')
s3 = session.client('s3')

# Nome do bucket
nome_bucket = 'bucket-boto3-desafio'

# Criando o Bucket com o nome informado
s3.create_bucket(Bucket=nome_bucket)

print(f"Bucket {nome_bucket} criado com sucesso!")

# Arquivo que será subido para o bucket
arquivo = 'SINPA_QUANTIDADE_PASSAPORTES_2024_10.csv'

# Nome do arquivo que será baixado do Bucket
download = 'SINPA_dowload'

# Subindo o arquivo de databases para o Bucket
s3.upload_file(arquivo, nome_bucket, arquivo)
print(f'O arquivo: {arquivo} foi enviado ao Bucket')

# Baixando o arquivo de emissões de passaporte com o nome SINPA_dowload
s3.download_file(nome_bucket, arquivo, download)
print(f'O arquivo {download} foi baixado com sucesso')
print()
print("O arquivo será analisado...")

# trazendo o arquivo para um dataframe
data = pd.read_csv(download,  sep=';', encoding='latin1')


# Copiando o data frame para emissoes
# Clausulas condicionais com dois operadores lógicos
emissoes = data[(data['ANO'] >= 2020) & (data['TIPO_PASSAPORTE'].str.contains('EMERGÊNCIA', case = False, na=False))].copy()


# clausula condicional
emissoes['DEMANDA'] = emissoes['QTD'].apply(lambda x: 'ALTA DEMANDA' if x > 100 else 'BAIXA DEMANDA')


# Função de agregação (soma por ano e estado)
emissoes_grup = emissoes.groupby(['ANO', 'UF'])['QTD'].sum().reset_index()


# Função de agregação para calcular a media de passaportes de emergencia emitidos
media_emergencia = emissoes.groupby('ANO')['QTD'].mean().reset_index()
media_emergencia.rename(columns={'QTD': 'MEDIA_PASSAPORTES_EMERGÊNCIA'}, inplace=True)


# Fazendo o merge para adicionar a coluna de média no dataframe `emissoes_grup`
emissoes_grup = pd.merge(emissoes_grup, media_emergencia, on='ANO', how='left')
emissoes = pd.merge(emissoes, media_emergencia, on='ANO', how='left')
emissoes['MEDIA_PASSAPORTES_EMERGÊNCIA'] = emissoes['MEDIA_PASSAPORTES_EMERGÊNCIA'].round(2)


# Função de conversão convertendo ANO para string
emissoes_grup['ANO'] = emissoes_grup['ANO'].astype(str)


# Função de string convertendo tipo de passaporte para maiúsculas
emissoes['TIPO_PASSAPORTE'] = emissoes['TIPO_PASSAPORTE'].str.lower()


# Função DATA
emissoes['ANO'] = pd.to_datetime(emissoes['ANO'], format='%Y').dt.strftime('%y')


# Função de ordenação
emissoes_grup = emissoes_grup.sort_values(by='QTD', ascending=False)
emissoes = emissoes.sort_values(by='QTD', ascending=False)


emissoes.to_csv("emissoes_passaporte_emergencia.csv", index=False, sep=';', encoding='utf-8-sig')

print("Analise finalizada")

# Caminho do arquivo gerado
arquivo_saida = "emissoes_passaporte_emergencia.csv"

# Upload do arquivo para o bucket
s3.upload_file(arquivo_saida, nome_bucket, arquivo_saida)
print(f"O arquivo {arquivo_saida} foi enviado para o bucket {nome_bucket} com sucesso!")
