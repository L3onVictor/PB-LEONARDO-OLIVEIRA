select nome
from autor left join livro on autor.codautor = livro.autor 
GROUP by codautor 
having count(livro.titulo) = 0
order by nome