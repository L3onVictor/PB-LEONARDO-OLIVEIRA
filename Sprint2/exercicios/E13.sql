select cdpro, 
nmcanalvendas, 
nmpro, 
SUM(qtd) as quantidade_vendas 
from tbvendas
where tbvendas.status = 'Concluído'
group by cdpro, nmcanalvendas, nmpro 
order by quantidade_vendas limit 10