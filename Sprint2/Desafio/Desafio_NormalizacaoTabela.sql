drop table if exists clientes;
drop table if exists carros;
drop table if exists combustivel;
drop table if exists locacao;
drop table if exists vendedores;

--Criação da tabela 'clientes'
CREATE table clientes(
idCliente int primary key,
nomeCliente varchar(255) not null,
cidadeCliente varchar(200) not null,
estadoCliente varchar(50)not null,
paisCliente varchar(50)not null
);

--Criação da tabela 'combustivel'
create table combustivel(
idCombustivel int primary key,
tipoCombustivel varchar(80)
);

--Criação da tabela 'carro'
create table carros(
idCarro int primary key,
kmCarro int,
classiCarro varchar(50),
marcaCarro varchar(80),
modeloCarro varchar(50) not null,
anoCarro int not null,
idCombustivel int,
foreign key (idCombustivel) references combustivel(idCombustivel)
);

--Criação da tabela 'vendedores'
create table vendedores(
idVendedor int primary key,
nomeVendedor varchar(255),
sexoVendedor smallint,
estadoVendedor varchar(80)
);

--Criação da tabela 'locacao'
create table locacao(
idLocacao int primary key,
idCliente int,
dataLocacao datetime,
horaLocacao time,
idCarro int,
qtdDiaria int,
vlrDiaria decimal,
dataEntrega date,
horaEntrega time,
idVendedor int,
FOREIGN KEY (idCliente) REFERENCES clientes(idCliente),
FOREIGN KEY (idVendedor) REFERENCES vendedores(idVendedor)
FOREIGN KEY (idCarro) REFERENCES carros(idCarro)
);

--inserções da tabela tb_locacao para a tabela clientes
INSERT INTO clientes (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao
GROUP BY idCliente;

INSERT INTO combustivel (idCombustivel,tipoCombustivel)
SELECT idCombustivel, tipoCombustivel
FROM tb_locacao 
GROUP BY idCombustivel;

INSERT INTO carros (idCarro,kmCarro,classiCarro,marcaCarro,modeloCarro,anoCarro,idCombustivel)
SELECT idCarro,kmCarro,classiCarro,marcaCarro,modeloCarro,anoCarro,idCombustivel
FROM tb_locacao
GROUP BY idCarro; 

INSERT INTO vendedores (idVendedor,nomeVendedor,sexoVendedor,estadoVendedor)
SELECT idVendedor,nomeVendedor,sexoVendedor,estadoVendedor 
FROM tb_locacao 
GROUP BY idVendedor;

INSERT INTO locacao (idLocacao, idCliente, dataLocacao, horaLocacao, idCarro,qtdDiaria,vlrDiaria, dataEntrega, horaEntrega, idVendedor)
SELECT idLocacao, idCliente, date(SUBSTRING(CAST(dataLocacao AS text ), 1, 4) || '-' || 
SUBSTRING(CAST(dataLocacao AS text),5,2) || '-' ||
SUBSTRING(CAST(dataLocacao AS text),7,2)) AS dataLocacao, horaLocacao, idCarro, qtdDiaria, vlrDiaria, 
DATE(SUBSTRING(dataEntrega, 1,4) || '-'|| 
SUBSTRING(dataEntrega,5,2) || '-' ||
SUBSTRING(dataEntrega, 7,2)) AS dataEntrega, horaEntrega, idVendedor
FROM tb_locacao 
GROUP BY idLocacao;