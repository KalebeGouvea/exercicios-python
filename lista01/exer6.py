#Calcule o tempo de uma viagem de carro. Pergunte a distância a 
#percorrer e a velocidade média esperada para a viagem.

dist = int(input('Informe a distância a percorrer (em km): '))
vel = int(input('Informe a velocidade média (em km/h): '))
tempo = (dist/vel)*60

print(f'O tempo da viagem será: {tempo:.0f} minutos.')