#Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e 
#também divisíveis por 7?

n = 0
for x in range(1067, 3628):
    if x % 2 == 0 and x % 7 == 0:
        n += 1

print(n)