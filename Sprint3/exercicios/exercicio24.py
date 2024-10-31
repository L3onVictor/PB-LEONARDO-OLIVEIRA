class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        lista = self.listaBaguncada
        lista.sort()
        return lista

    def ordenacaoDecrescente(self):
        lista = self.listaBaguncada
        lista.sort(reverse=True)
        return lista
        
crescente = Ordenadora([3,4,2,1,5])

decrescente = Ordenadora([9,7,6,8])

print(crescente.ordenacaoCrescente())

print(decrescente.ordenacaoDecrescente())