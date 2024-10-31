import random

random_list = random.sample(range(500), 50)

listaOrdernada = sorted(random_list)

quant = len(listaOrdernada)

if(quant %2 == 0):
    mediana = (listaOrdernada[quant // 2-1] + listaOrdernada[quant // 2]) / 2
   

else:
    mediana = listaOrdernada[quant // 2]

media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')