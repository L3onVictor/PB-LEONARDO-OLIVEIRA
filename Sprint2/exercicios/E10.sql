select tbvendedor.nmvdd as vendedor, 
SUM(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas,
round(SUM((tbvendas.qtd * tbvendas.vrunt) * (tbvendedor.perccomissao / 100.0)), 2) as comissao
from tbvendedor left join tbvendas 
on tbvendedor.cdvdd = tbvendas.cdvdd 
and tbvendas.status = 'Concluído'
group by tbvendedor.nmvdd
order by comissao desc

select nmvdd, perccomissao, (perccomissao/100.0) as comissao 
from tbvendedor t 