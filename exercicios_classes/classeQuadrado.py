"""
2. Classe Quadrado: Crie uma classe que modele um quadrado:
a. Atributos: Tamanho do lado
b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def mudaLado(self, lado):
        self.lado = lado
    
    def retornaLado(self):
        return self.lado
    
    def calculaArea(self):
        return self.lado*self.lado

quadrado = Quadrado(2)
print (quadrado.retornaLado())
print (quadrado.calculaArea())

quadrado.mudaLado(4)
print (quadrado.retornaLado())
print (quadrado.calculaArea())
