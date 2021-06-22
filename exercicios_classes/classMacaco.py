"""
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) 
e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste 
interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 
3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []
    
    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        if len(self.bucho) > 0:
            self.bucho.clear()

m1 = Macaco("Caesar")
m2 = Macaco("Koba")

m1.comer("banana")
print(m1.verBucho())

m1.comer("manga")
print(m1.verBucho())

m1.comer("abacate")
print(m1.verBucho())

m1.digerir()
print(m1.verBucho())

m2.comer("formigas")
print(m2.verBucho())

m2.comer("caju")
print(m2.verBucho())

m2.comer("goiaba")
print(m2.verBucho())

m2.comer(m1)
print(m2.verBucho())