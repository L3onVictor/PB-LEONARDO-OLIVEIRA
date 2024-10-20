select nmcli, cdcli, SUM(vrunt*qtd) as gasto
from tbvendas
where status = 'Concluído'
group by cdcli 
order by gasto desc limit 1