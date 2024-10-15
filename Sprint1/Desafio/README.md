# Desafio
Foi solicitado a criação de um script no Linux, ***processamento_de_vendas.sh***, que: *Crie um diretório chamado vendas, crie um subdiretório chamado backup, faça uma cópia do arquivo* **dados_de_vendas.csv** *para o subdiretório backup e renomeie o arquivo para* **dados-yyyymmdd.csv**. *Dentro do diretório backup, renomeie-o para* **backup-dados-yyyymmdd.csv**. *Ainda na pasta* **backup**, *crie um arquivo* **relatorio.txt** *com as seguintes informações:*
- Data atual do sistema: yyyymmdd
- Data do primeiro registro
- Data do último registro
- Quantidade total de itens diferentes vendidos
- Exibir as 10 primeiras linhas do arquivo **backup-dados-yyyymmdd.csv**

Compacte os arquivos **backup-dados-yyyymmdd.csv** e **dados_de_vendas.csv** em ***.zip***, apague o arquivo **backup-dados-yyyymmdd.csv** do diretório ***backup*** e o **dados_de_vendas.csv** do diretório ***vendas***.

Agende uma execução de quatro dias no crontab às 15:27h.

Ao final, crie outro script ***consolidados_de_processamento_de_vendas.sh*** que una todos os relatórios gerados. Após a execução dos 4 dias do ***processamento_de_vendas.sh***, execute esse script manualmente para unir os relatórios gerados.

### Na pasta ```dados_de_vendas_alteracao.csv``` estão todas as alterações realizadas no arquivo ```dados_de_vendas.csv``` ao longo do desafio.

# Etapa 1
Criando o código do executável ***processamento_de_vendas.sh***
![códigoProcessamento](../evidencias/script_codigo.png)
Esse script realiza as seguintes tarefas:
- Cria a pasta **vendas** dentro da pasta **ecommerce** e copia o arquivo **dados_de_vendas.csv** para ela.
- Entra no diretório vendas, cria o subdiretório backup, copia e renomeia o arquivo **dados_de_vendas** para **backup-dados-yyyymmdd**.
- Cria um relatório com a data atual ***relatorio-yyyymmdd.txt***.
- Preenche esse relatório com as seguintes informações:
    - Data atual do sistema.
    - Primeiro e último registro de venda.
    - Quantidade de itens diferentes vendidos.
    - As primeiras 10 (dez) linhas do arquivo **backup-dados-yyyymmdd**.

- Após isso, compacta o arquivo **backup-dados-yyyymmdd** para **backup-dados-yyyymmdd.zip**.

- E remove os arquivos **backup-dados-yyyymmdd** e **dados_de_vendas.csv** do diretório **vendas**.

## Modelo do primeiro relatório criado
![Primeiro relatório](../evidencias/relatorio01.png)
Os relatórios são preenchidos adequadamente. Foram gerados mais 3 relatórios com as alterações no arquivo **dados_de_vendas.csv**.

# Etapa 2
Após a primeira execução, é necessário alterar manualmente o arquivo **dados_de_vendas.csv** para novos itens vendáveis.

## Mudanças no arquivo dados_de_vendas
#### Arquivo original
![Dados de vendas1](../evidencias/dados_vendas01.png)
#### Primeira mudança (Instrumentos musicais e afins)
![Dados de vendas2](../evidencias/dados_vendas02.png)
#### Segunda mudança (Cesta básica)
![Dados de vendas3](../evidencias/dados_vendas03.png)
#### Terceira e última mudança (PCs e itens relacionados à tecnologia)
![Dados de vendas4](../evidencias/dados_vendas04.png)

# Etapa 3
Com isso, foram gerados mais relatórios com cada uma das mudanças acima informadas.

### Relatório criado com itens de instrumentos musicais e afins
![Relatório instrumentos](../evidencias/relatorio02.png)
### Relatório criado com itens de cesta básica
![Relatório cesta](../evidencias/relatorio03.png)
### Relatório criado com itens de tecnologia e afins
![Relatório tecnologia](../evidencias/relatorio04.png)
Contando com o ```Modelo do primeiro relatório```, são 4 relatórios no total.

# Etapa 4
Para essa etapa, foi necessário automatizar o script. Para isso, foi agendado um horário no crontab para que o script seja executado de maneira automática.
![Crontab](../evidencias/crontab.png) 
Esse crontab está agendado para executar o script ```processamento_de_dados.sh``` com a seguinte formatação: às 15:27 horas, em qualquer dia do mês, em qualquer mês, entre os dias da semana de quarta a domingo.


# Etapa 5
Após as 4 execuções, deve-se criar um executável chamado **consolidador_de_processamentos_de_vendas.sh** que irá unir todos os 4 relatórios em um arquivo ***relatorio_final.txt***.

### Código do consolidador
![Consolidador](../evidencias/consolidador.png)
Esse código coleta todos os arquivos de relatórios (independentemente do que vier após o " - ") e armazena no arquivo ```relatorio_final.txt```.

Parte do **relatorio_final.txt**
![Relatório final](../evidencias/cat_relatorioFinal.png)

## Criação dos arquivos na pasta ecommerce

Aqui está a criação de cada arquivo visualizada com o ```tree``` na pasta ```ecommerce```.

1. Primeira execução do crontab
![Crontab1](../evidencias/tree_execucao01.png)

2. Segunda execução do crontab
![Crontab2](../evidencias/tree_execucao02.png)

3. Terceira execução do crontab
![Crontab3](../evidencias/tree_execucao03.png)

4. Quarta execução do crontab
![Crontab4](../evidencias/tree_execucao04.png)

5. Criação do ```relatorio_final.txt``` e conclusão do desafio.
![Relatório final](../evidencias/relatorioFinal.png)
