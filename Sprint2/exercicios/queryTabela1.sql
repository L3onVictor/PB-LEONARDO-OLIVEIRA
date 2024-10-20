SELECT cod AS CodLivro, 
titulo, 
autor.codautor , 
autor.nome AS NomeAutor, 
Valor,
editora.codeditora , 
editora.nome AS NomeEditora
FROM livro
LEFT JOIN autor  ON autor.codautor = LIVRO.autor
LEFT JOIN editora ON editora.codeditora = LIVRO.editora 
GROUP BY livro.cod, livro.titulo 
ORDER BY LIVRO.valor DESC 
LIMIT 10