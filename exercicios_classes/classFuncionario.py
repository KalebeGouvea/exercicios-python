# -*- coding: utf-8 -*-
"""
13. Classe Funcionário: Implemente a classe Funcionário. Um empregado 
tem um nome (um string) e um salário(um double). Escreva um 
construtor com dois parâmetros (nome e salário) e métodos para 
devolver nome e salário. Escreva um pequeno programa que teste sua classe.

14. Aprimore a classe do exercício anterior para adicionar o método 
aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário 
em uma certa porcentagem.
- Exemplo de uso:
- harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)
"""

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def obterNome(self):
        return self.nome
    
    def obterSalario(self):
        return self.salario
    
    def aumentarSalario(self, porc):
        self.salario *= (1 + porc/100)

func01 = Funcionario("Francisley", 4250.50)
print("Nome do funcionário: ", func01.obterNome())
print("Salário do funcionário: ", func01.obterSalario())
func01.aumentarSalario(10)
print("Salário do funcionário: ", func01.obterSalario())
