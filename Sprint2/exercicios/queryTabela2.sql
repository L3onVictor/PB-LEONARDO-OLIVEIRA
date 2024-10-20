select codeditora,
nome as NomeEditora,
count(livro.cod) as QuantidadeLivros
from editora 
left join livro on editora.codeditora = livro.editora
GROUP BY codeditora, nome 
HAVING count(livro.cod) > 0
order by QuantidadeLivros DESC 
limit 5
