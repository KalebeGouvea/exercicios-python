# -*- coding: utf-8 -*-
"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
a. Atributos: Nome, Fome, Saúde e Idade 
b. Métodos: Alterar Nome, Fome, Saúde e Idade; 
Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar 
em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os 
atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo 
para armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""

class Tamagushi:
    def __init__(self, nome, idade, fome, saude):
        self.mudarNome(nome)
        self.mudarIdade(idade)
        #Atributo fome: maior é melhor
        self.mudarFome(fome)
        #Atributo saúde: maior é melhor
        self.mudarSaude(saude)
    
    def mudarNome(self, nome):
        self.nome = nome

    def mudarIdade(self, idade):
        self.idade = idade

    def mudarFome(self, fome):
        self.fome = fome
    
    def mudarSaude(self, saude):
        self.saude = saude
    
    def obterNome(self):
        return self.nome
    
    def obterIdade(self):
        return self.idade
    
    def obterFome(self):
        return self.fome
    
    def obterSaude(self):
        return self.saude
    
    def obterHumor(self):
        return self.obterSaude() * self.obterFome()

bichinho = Tamagushi("Horácio", 0, 100, 100)
#Print que testa o retorno dos métodos
print(bichinho.obterNome(), bichinho.obterIdade(), bichinho.obterFome(), bichinho.obterSaude(), bichinho.obterHumor())

#Mudando atributos através dos métodos
bichinho.mudarNome("Pingo")
bichinho.mudarIdade(5)
bichinho.mudarSaude(90)
bichinho.mudarFome(90)

print(bichinho.obterNome(), bichinho.obterIdade(), bichinho.obterFome(), bichinho.obterSaude(), bichinho.obterHumor())