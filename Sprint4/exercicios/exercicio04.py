def calcular_valor_maximo(operadores,operandos) -> float:
    resultado = map(
        lambda valor: valor[1][0] + valor[1][1] if valor[0] == '+' 
        else valor[1][0] - valor[1][1] if valor[0] == '-' 
        else valor[1][0] * valor[1][1] if valor[0] == '*' 
        else valor[1][0] / valor[1][1] if valor[0] == '/' 
        else valor[1][0] % valor[1][1] if valor[0] == '%' 
        else None,
        zip(operadores, operandos)
    )
    
    return max(resultado)
    
operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

print(calcular_valor_maximo(operadores, operandos))