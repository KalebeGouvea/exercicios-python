# -*- coding: utf-8 -*-
"""
Faça uma classe contaInvestimento que seja semelhante a classe 
contaBancaria, com a diferença de que se adicione um atributo 
taxaJuros. Forneça um construtor que configure tanto o saldo 
inicial como a taxa de juros. Forneça um método adicioneJuros 
(sem parâmetro explícito) que adicione juros à conta. Escreva 
um programa que construa uma poupança com um saldo inicial de 
R$1000,00 e uma taxa de juros de 10%. Depois aplique o método 
adicioneJuros() cinco vezes e imprime o saldo resultante.
"""

class ContaCorrente:
    def __init__(self, conta, nome, saldo = 0):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        self.saldo += valor

    #O método saque admite que o cliente pode ficar negativo com o banco
    def saque(self, valor):
        self.saldo -= valor

class contaInvestimento(ContaCorrente):
    def __init__(self, conta, nome, saldo, taxaJuros):
        ContaCorrente.__init__(self, conta, nome, saldo)
        self.taxaJuros = taxaJuros
    
    def adicioneJuros(self):
        self.saldo = self.saldo*(1 + self.taxaJuros/100)

poupanca = contaInvestimento(1234, "Juscelino", 1000, 10)
poupanca.adicioneJuros()
poupanca.adicioneJuros()
poupanca.adicioneJuros()
poupanca.adicioneJuros()
poupanca.adicioneJuros()
print(vars(poupanca))