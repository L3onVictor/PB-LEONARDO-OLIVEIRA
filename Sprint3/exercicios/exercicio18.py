speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
listaValor = set()
for i in speed:
    if speed[i] not in listaValor:
        listaValor.add(speed[i])
print(sorted(list(listaValor)))