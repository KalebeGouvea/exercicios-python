#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos 
#do usuário. Calcule o total em segundos.

d = int(input('Dias: ')) * 86400
h = int(input('Horas: ')) * 3600
m = int(input('Minutos: ')) * 60
s = int(input('Segundos: '))
total = d + h + m + s
print ('Total em segundos: ' + str(total))