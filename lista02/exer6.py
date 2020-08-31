"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 
5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou 
ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário 
Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, 
conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
"""
shora = float(input('Digite o salário/hora: '))
nhora = int(input('Digite o número de horas trabalhadas/mês: '))
bruto = shora * nhora
inss = bruto * 0.08
ir = bruto * 0.11
sind = bruto * 0.05
liquido = bruto - inss - ir - sind

print(f'+ Salário Bruto :\t R$ {bruto:.2f}')
print(f'- IR :\t\t\t R$ {ir:.2f}')
print(f'- INSS :\t\t R$ {inss:.2f}')
print(f'- Sindicato :\t\t R$ {sind:.2f}')
print(f'= Salário Líquido :\t R$ {liquido:.2f}')