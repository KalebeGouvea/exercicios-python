# -*- coding: utf-8 -*-
"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar 
o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume 
permanecem dentro de faixas válidas.
"""
class TV:
    def __init__(self):
        self.canal = 0
        self.volume = 0

    def mudarCanal (self, canal):
        #Número do canal superior a zero
        if canal > 0:
            self.canal = canal
    
    def aumentarVolume (self):
            #Volume máximo: 100
            if self.volume < 100:
                self.volume += 1
    
    def diminuirVolume (self):
            #Volume mínimo: 0
            if self.volume > 0:
                self.volume -= 1

#Criando TV como objeto
tv = TV()
print(vars(tv))

#Mudando o canal e aumentando o volume
tv.mudarCanal(342)
tv.aumentarVolume()
print(vars(tv))

#Diminuindo o volume
tv.diminuirVolume()
print(vars(tv))