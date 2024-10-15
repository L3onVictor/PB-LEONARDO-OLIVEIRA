SELECT count(livro.cod) as quantidade, nome, endereco.estado, endereco.cidade
from editora inner join livro on editora.codeditora = livro.editora
inner join endereco on endereco.codendereco = editora.endereco
group by editora.codeditora, editora.nome, endereco.estado, endereco.cidade
order by quantidade desc limit 5
