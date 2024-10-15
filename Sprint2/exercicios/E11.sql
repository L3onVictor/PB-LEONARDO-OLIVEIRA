select cdcli, nmcli, SUM(qtd*vrunt) as gasto
from tbvendas
where status = 'Concluído'
group by nmcli 
order by gasto desc 