drop table if exists dim_clientes;
drop table if exists dim_carros;
drop table if exists dim_combustivel;
drop table if exists dim_vendedores;
drop table if exists fato_locacao;

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
idCliente int,
dataLocacao datetime,
horaLocacao time,
idCarro int,
qtdDiaria int,
vlrDiaria decimal,
dataEntrega date,
horaEntrega time,
idVendedor int,
FOREIGN KEY (idCliente) REFERENCES dim_clientes(idCliente),
FOREIGN KEY (idVendedor) REFERENCES dim_vendedores(idVendedor)
FOREIGN KEY (idCarro) REFERENCES dim_carros(idCarro)
);

--View para ver a locacao realizada
CREATE VIEW locacaoCompleta_view AS SELECT 
    cliente.nomeCliente,
    vendedor.nomeVendedor,
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
CREATE VIEW dataLocacao_view AS SELECT 
idLocacao,
dataLocacao,
horaLocacao,
dataEntrega,
horaEntrega
FROM fato_locacao;

--View para ver detalhes sobre o carro
CREATE view detalheCarro_view AS SELECT 
idCarro,
marcaCarro,
classiCarro,
kmCarro,
combustivel.tipoCombustivel,
modeloCarro,
anoCarro
FROM dim_carros AS carro LEFT JOIN dim_combustivel AS combustivel
ON carro.idCombustivel = combustivel.tipoCombustivel;