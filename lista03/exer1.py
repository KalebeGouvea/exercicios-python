#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso 
#o valor seja inválido e continue pedindo até que o usuário informe um valor 
#válido.

nota = float(input('Digite um número entre zero e dez: '))
while not (nota >= 0 and nota <= 10):
    print ('Valor inválido')
    nota = float(input('Digite um número entre zero e dez: '))
print('Valor válido')
