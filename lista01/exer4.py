#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor 
#do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

sal = float(input('Insira o valor do salário: '))
porc = float(input('Insira a porcentagem do aumento (em %): '))/100
aumento = round(sal * porc, 2)
novo_sal = round(sal + aumento, 2)

print (f'O aumento foi de R$ {aumento:.2f}') 
print (f'O novo salário é de R$ {novo_sal:.2f}')