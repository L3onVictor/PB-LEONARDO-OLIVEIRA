#!/bin/bash

#Cria o diretorio vendas no ecommerce e copia o dados_de_vendas para ele
mkdir -p /home/leonardo/ecommerce/vendas
cp  /home/leonardo/ecommerce/dados_de_vendas.csv /home/leonardo/ecommerce/vendas/

#Entra no diretorio vendas, cria o subdiretorio backup copia e renomeia o arquivo dados_de_vendas para backup-dados-yyymmdd
cd  /home/leonardo/ecommerce/vendas/
mkdir -p backup
cp dados_de_vendas.csv backup/dados-$(date +%Y%m%d).csv
mv backup/dados-$(date +%Y%m%d).csv backup/backup-dados-$(date +%Y%m%d).csv

#Cria um relatorio com a data atual
touch backup/relatorio-$(date +%Y%m%d).txt

#Apenas remove o cabeçalho
Datas=$(tail -n +2 dados_de_vendas.csv)

#Captura a primeira e a ultima linha
Primeiro_registro=$(echo "$Datas" | head -n1 | cut -d, -f5)
Ultimo_registro=$(echo "$Datas" | tail -n1 | cut -d, -f5)

#Preenche o relatorio com: a data atual do sistema, primeiro e ultimo registro de venda, quantidade de itens diferentes vendidos e primeiras 10 linhas do arquivo de backup
echo "Data do sistema atual: $(date +%Y/%m/%d' '%H:%M)" >> backup/relatorio-$(date +%Y%m%d).txt
echo "Data do primeiro registro de venda: $Primeiro_registro" >> backup/relatorio-$(date +%Y%m%d).txt
echo "Data do ultimo registro de venda: $Ultimo_registro" >> backup/relatorio-$(date +%Y%m%d).txt
echo "Quantidades de items diferentes vendidos: $(tail -n +2 dados_de_vendas.csv | wc -l)" >> backup/relatorio-$(date +%Y%m%d).txt
echo -e "Primeiras 10 linhas do backup:\n$(head backup/backup-dados-$(date +%Y%m%d).csv)\n" >> backup/relatorio-$(date +%Y%m%d).txt

#Zipa os arquivos de backup
zip -r backup/backup-dados-$(date +%Y%m%d).zip backup/backup-dados-$(date +%Y%m%d).csv

#Remove os arquivos de backup-dados-yyyymmdd e dados_de_vendas do diretorio vendas
rm backup/backup-dados-$(date +%Y%m%d).csv && rm dados_de_vendas.csv
cd ..
