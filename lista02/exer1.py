#Faça um Programa que peça os três lados de um triângulo. O programa deverá 
#informar se os valores podem ser um triângulo. Indique, caso os lados formem 
#um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

l1 = float(input('Insira a medida do primeiro lado: '))
l2 = float(input('Insira a medida do segundo lado: '))
l3 = float(input('Insira a medida do terceiro lado: '))

if l1>l2+l3 or l2>l1+l3 or l3>l1+l2:
    print('Não é um triângulo')
elif l1 == l2 == l3:
    print('É um triângulo equilátero')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('É um triângulo isósceles')
else:
    print('É um triângulo escaleno')