drop table if exists dim_clientes;
drop table if exists dim_carros;
drop table if exists dim_combustivel;
drop table if exists dim_vendedores;
drop table if exists fato_locacao;

DROP VIEW IF exists vw_dataLocacao;
DROP VIEW IF EXISTS vw_detalheCarro;
DROP VIEW IF EXISTS vw_locacaoCompleta;
DROP VIEW IF EXISTS vw_carroMaisRecente;

--Criação da dimensão 'Clientes'
CREATE TABLE dim_clientes(
idCliente int primary key,
nomeCliente varchar(255) not null,
cidadeCliente varchar(200) not null,
estadoCliente varchar(50)not null,
paisCliente varchar(50)not null
);

--Criação da dimensão 'Combustivel'
create table dim_combustivel(
idCombustivel int primary key,
tipoCombustivel varchar(80)
);

--Criação da dimensão 'carro'
create table dim_carros(
idCarro int primary key,
kmCarro int,
classiCarro varchar(50),
marcaCarro varchar(80),
modeloCarro varchar(50) not null,
anoCarro int not null,
idCombustivel int,
foreign key (idCombustivel) references dim_combustivel(idCombustivel)
);

--Criação da dimensão 'vendedores'
create table dim_vendedores(
idVendedor int primary key,
nomeVendedor varchar(255),
sexoVendedor smallint,
estadoVendedor varchar(80)
);


--Criação da dimensão 'locacao'
create table fato_locacao(
idLocacao int primary key,
dataLocacao datetime,
horaLocacao time,
idCliente int,
idData int,
idCarro int,
qtdDiaria int,
vlrDiaria decimal,
dataEntrega date,
horaEntrega time,
idVendedor int,
FOREIGN KEY (idCliente) REFERENCES dim_clientes(idCliente),
FOREIGN KEY (idVendedor) REFERENCES dim_vendedores(idVendedor),
FOREIGN KEY (idCarro) REFERENCES dim_carros(idCarro)
);


--inserções da tabela tb_locacao para a tabela clientes
INSERT INTO dim_clientes (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao
GROUP BY idCliente;

INSERT INTO dim_combustivel (idCombustivel,tipoCombustivel)
SELECT idCombustivel, tipoCombustivel
FROM tb_locacao 
GROUP BY idCombustivel;

INSERT INTO dim_carros (idCarro,kmCarro,classiCarro,marcaCarro,modeloCarro,anoCarro,idCombustivel)
SELECT idCarro,kmCarro,classiCarro,marcaCarro,modeloCarro,anoCarro,idCombustivel
FROM tb_locacao
GROUP BY idCarro; 

INSERT INTO dim_vendedores (idVendedor,nomeVendedor,sexoVendedor,estadoVendedor)
SELECT idVendedor,nomeVendedor,sexoVendedor,estadoVendedor 
FROM tb_locacao 
GROUP BY idVendedor;

INSERT INTO fato_locacao (idLocacao, idCliente, dataLocacao, horaLocacao, idCarro,qtdDiaria,vlrDiaria, dataEntrega, horaEntrega, idVendedor)
SELECT idLocacao, idCliente, date(SUBSTRING(CAST(dataLocacao AS text ), 1, 4) || '-' || 
SUBSTRING(CAST(dataLocacao AS text),5,2) || '-' ||
SUBSTRING(CAST(dataLocacao AS text),7,2)) AS dataLocacao, horaLocacao, idCarro, qtdDiaria, vlrDiaria, 
DATE(SUBSTRING(dataEntrega, 1,4) || '-'|| 
SUBSTRING(dataEntrega,5,2) || '-' ||
SUBSTRING(dataEntrega, 7,2)) AS dataEntrega, horaEntrega, idVendedor
FROM tb_locacao 
GROUP BY idLocacao;


--View para ver a locacao realizada
CREATE VIEW vw_locacaoCompleta AS SELECT 
    cliente.idCliente,
	cliente.nomeCliente,
	vendedor.idVendedor,
    vendedor.nomeVendedor,
    fato.idLocacao,
    carro.marcaCarro,
    carro.modeloCarro,
    comb.tipoCombustivel,
    fato.dataLocacao,
    fato.qtdDiaria,
    (fato.qtdDiaria * fato.vlrDiaria) AS valorTotalLocacao
FROM fato_locacao AS fato
JOIN dim_clientes AS cliente ON fato.idCliente = cliente.idCliente
JOIN dim_vendedores AS vendedor ON fato.idVendedor = vendedor.idVendedor
JOIN dim_carros as carro ON fato.idCarro = carro.idCarro
JOIN dim_combustivel AS comb ON carro.idCombustivel = comb.idCombustivel;

--view para ver a data e hora da locacao e da entrega
CREATE VIEW vw_dataLocacao AS SELECT 
idLocacao,
dataLocacao,
horaLocacao,
dataEntrega,
horaEntrega
FROM fato_locacao; 

-- view para ver o carro mais 'novo'
CREATE VIEW vw_carroMaisRecente AS SELECT
idCarro,
marcaCarro,
classiCarro,
modeloCarro,
kmCarro,
comb.tipoCombustivel,
anoCarro
FROM dim_carros AS carro LEFT JOIN dim_combustivel AS comb
ON carro.idCombustivel = comb.idCombustivel
ORDER BY carro.anoCarro DESC 
LIMIT 1;

--View para ver detalhes sobre o carro
CREATE view vw_detalheCarro AS SELECT 
idCarro,
marcaCarro,
classiCarro,
kmCarro,
combustivel.tipoCombustivel,
modeloCarro,
anoCarro
FROM dim_carros AS carro LEFT JOIN dim_combustivel AS combustivel
ON carro.idCombustivel = combustivel.idCombustivel;

SELECT * FROM vw_detalheCarro vdc 