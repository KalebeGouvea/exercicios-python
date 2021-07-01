# -*- coding: utf-8 -*-
"""
2. Classe Quadrado: Crie uma classe que modele um quadrado:
a. Atributos: Tamanho do lado
b. Metodos: Mudar valor do Lado, Retornar valor do Lado e calcular Area;
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

#Utilizando metodos para retornar a medida do quadrado e sua area
quadrado = Quadrado(2)
print (quadrado.retornaLado())
print (quadrado.calculaArea())

#Utilizando metodos para mudar lado do quadrado, retornar a medida do lado e calcular a area
quadrado.mudaLado(4)
print (quadrado.retornaLado())
print (quadrado.calculaArea())
