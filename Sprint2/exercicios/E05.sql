select autor.nome 
from livro 
inner join autor on autor.codautor = livro.autor 
INNER join editora on editora.codeditora = livro.editora 
INNER join endereco on editora.endereco = endereco.codendereco 
where endereco.estado not in ('PARANÁ', 'RIO GRANDE DO SUL')
GROUP by autor.nome
order by autor.nome 