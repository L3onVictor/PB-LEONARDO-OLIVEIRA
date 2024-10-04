# Desafio
Foi pedido a criação de um Script no Linux, ***processamento_de_vendas.sh***, que: *Cria um diretório chamado vendas, cria um subdiretório chamado backup, faça uma copia do arquivo* **dados_de_vendas.csv** *para o subdiretório backup e renomear o arquivo para* **dados-yyyymmdd.csv** *e, dentro do diretorio backup, renomea-lo para* **backup-dados-yyyymmdd.csv**. *Dentro da pasta* **backup** *criar um arquivo* **relatorio.txt** *que contenha:*
- data do sistema atual: yyyymmdd
- data do primeiro registro
- data do ultimo registro
- quantidade total de intens diferentes vendidos
- mostrar as 10 primwiras linhas do arquivo **backup-dados-yyyymmdd.csv**

Compactar os arquivos **backup-dados-yyyymmdd.csv** e **dados_de_vendas.csv** em ***.zip*** e apagar o arquivo **backup-dados-yyyymmdd.csv** do diretorio ***backup*** e o **dados_de_vendas.csv** do diretorio ***vendas***.

Agendar uma execução de quatro dias no crontab às 15:27 h 

Ao final, criar outro Script ***consolidados_de_processamento_de_vendas.sh*** que una todos os relatorios gerados. Apos a execução dos 4 dias do ***processamento_de_vendas.sh***, executar esse Script para unir os relatorios gerados
# Etapa 1