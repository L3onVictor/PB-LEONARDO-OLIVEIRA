from functools import reduce

def calcula_saldo(lancamentos) -> float:

    valor = map(lambda x: -x[0] if x[1] == 'D' else x[0], lancamentos)
    
    resultado = reduce(lambda x, y: x + y, valor)
    
    return resultado

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

print(calcula_saldo(lancamentos))