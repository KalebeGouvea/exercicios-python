# -*- coding: utf-8 -*-
"""
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
a.Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa 
quantidade de combustível no tanque.
b.O consumo é especificado no construtor e o nível de combustível inicial é 0.
c.Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, 
reduzindo o nível de combustível no tanque de gasolina.
d.Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
e.Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
f. meuFusca = Carro(15);            #15 quilômetros por litro de combustível.
g. meuFusca.adicionarGasolina(20);  #abastece com 20 litros de combustível.
h. meuFusca.andar(100);             #anda 100 quilômetros.
meuFusca.obterGasolina()            #Imprime o combustível que resta no tanque.
"""

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0
    
    def andar(self, distancia):
        consumido = distancia/self.consumo
        diferenca = self.combustivel - consumido
        if diferenca >= 0:
            self.combustivel = diferenca
    
    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, litros):
        self.combustivel += litros

meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
print("Combustivel no tanque: ", meuFusca.obterGasolina())