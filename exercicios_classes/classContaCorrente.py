# -*- coding: utf-8 -*-
"""
5. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes 
atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; 
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
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

#Criado objeto cliente 1
cliente1 = ContaCorrente(12345, "Josefino", 500)

print(vars(cliente1))
cliente1.alterarNome("Robervaldo")
print(vars(cliente1))

cliente1.deposito(300)
print(vars(cliente1))

cliente1.saque(100)
print(vars(cliente1))

#Criado objeto cliente 2
cliente2 = ContaCorrente(54321, "Lúcia")
print(vars(cliente2))

cliente2.deposito(300)
print(vars(cliente2))

cliente2.saque(500)
print(vars(cliente2))