select codautor, nome, count(livro.titulo) as quantidade_publicacoes
from autor left join livro on autor.codautor = livro.autor 
GROUP by codautor 
order by quantidade_publicacoes desc 
limit 1