select tbvendas.cdvdd, tbvendedor.nmvdd 
from tbvendedor left join tbvendas on tbvendedor.cdvdd = tbvendas.cdvdd
and tbvendas.status = 'Concluído'
group by tbvendedor.nmvdd 
order by count(tbvendas.cdpro) DESC 
limit 1

