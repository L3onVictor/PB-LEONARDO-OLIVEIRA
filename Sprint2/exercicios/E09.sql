SELECT cdpro, nmpro from tbvendas
where status = 'Concluído' and dtven BETWEEN '2014-02-03' and '2018-02-02'
group by cdpro, nmpro 
order by COUNT(cdpro) DESC 
limit 1