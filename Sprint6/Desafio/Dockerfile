# Usando a imagem do python 3.9
FROM python:3.9

# Definindo o diretorio de trabalho
WORKDIR /app

# Copiando o arquivo requieiments
COPY requirements.txt .

# Baixando as dependencias do arquivo requirements
RUN pip install -r requirements.txt

# Copiando as credenciais da aws
COPY .aws /root/.aws

# Copiando o Script python que será executado no container
COPY Script.py .

# Definindo um volume
VOLUME [ "/data" ]

# Indica o caminho a ser executado, No caso: com o <Python>, execute o <Script.py>
CMD [ "python", "Script.py" ]