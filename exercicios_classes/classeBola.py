#Exercicios retirados da pagina https://wiki.python.org.br/ExerciciosClasses
"""
1. Classe Bola: Crie uma classe que modele uma bola:
a. Atributos: Cor, circunferencia, material
b. Metodos: trocaCor e mostraCor
"""
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor(self, cor):
        self.cor = cor
    
    def mostraCor(self):
        return self.cor

bola = Bola("amarela", 0.70, "couro")
print(bola.mostraCor())

bola.trocaCor("marrom")
print(bola.mostraCor())