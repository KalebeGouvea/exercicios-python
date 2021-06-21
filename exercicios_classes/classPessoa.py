"""
4. Classe Pessoa: Crie uma classe que modele uma pessoa:
a. Atributos: nome, idade, peso e altura
b.Metodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrao, a cada ano que nossa pessoa envelhece, 
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer (self, ano):
        if self.idade < 21:
            self.crescer(0.5*ano)
        self.idade += ano

    def engordar (self, quilos):
        self.peso += quilos

    def emagrecer (self, quilos):
        self.peso -= quilos

    def crescer (self, metros):
        self.altura += metros

ind = Pessoa("Fulano da Silva", 17, 78, 170)

print("O nome da pessoa é: ", ind.nome)

print ("O peso da pessoa é: ", ind.peso)
ind.engordar(10.5)
print ("O peso da pessoa agora é: ", ind.peso)

print ("O peso da pessoa é: ", ind.peso)
ind.emagrecer(5)
print ("O peso da pessoa agora é: ", ind.peso)

print ("A altura da pessoa é: ", ind.altura)
ind.crescer(2)
print ("A altura da pessoa agora é: ", ind.altura)

print ("A idade da pessoa é: ", ind.idade)
print ("A altura da pessoa é: ", ind.altura)
ind.envelhecer(3)
print ("A idade da pessoa agora é: ", ind.idade)
print ("A altura da pessoa agora é: ", ind.altura)