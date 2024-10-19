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
