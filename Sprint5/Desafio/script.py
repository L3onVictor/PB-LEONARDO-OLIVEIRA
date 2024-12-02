import pandas as pd

# trazendo o arquivo para um dataframe
data = pd.read_csv("Sprint5/Desafio/SINPA_QUANTIDADE_PASSAPORTES_2024_10.csv",  sep=';', encoding='latin1')


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

# Saida de todas as funções em conjuto
# print("Emissões Agrupadas e medias:")
# print(emissoes_grup)

# Tabela completa
# print("\nDetalhes das Emissões:")
# print(emissoes[['ANO','MES', 'UF', 'TIPO_PASSAPORTE', 'QTD', 'MEDIA_PASSAPORTES_EMERGÊNCIA', 'DEMANDA']])

emissoes.to_csv("emissoes_passaporte_emergencia.csv", index=False, sep=';', encoding='utf-8-sig')