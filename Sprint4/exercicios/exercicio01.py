with open('number.txt') as num:
    numeros = num.read().splitlines()
    
numerosList = map(int, numeros)
    
par = list(filter(lambda x: x%2==0, numerosList))

order_par = sorted(par, reverse=True)[:5]

soma = sum(order_par)

print(order_par)

print(soma)