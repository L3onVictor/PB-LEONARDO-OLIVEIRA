select nome, codautor, nascimento, count(livro.cod) as quantidade
from autor left join livro on autor.codautor = livro.autor
GROUP by autor.nome
order by autor.nome