class Aviao:
    cor = 'azul'
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        
    def toString(self):
        print(f'O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima}, capacidade para {self.capacidade} passageiros e é da cor {self.cor}.')

aviao1 = Aviao('BOIENG456', 1500, 400,)
aviao2 = Aviao("Embraer Praetor 600", 863, 14)
aviao3 = Aviao("Antonov An-2", 258, 12)

aviao1.toString()
aviao2.toString()
aviao3.toString()