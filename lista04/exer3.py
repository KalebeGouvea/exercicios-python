#Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. 
#Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos 
#elementos intercalados dos dois outros vetores. Imprima os três vetores.

from random import sample

lista1 = sample(range(100), 10)
lista2 = sample(range(100), 10)
lista3 = []

for x in range(10):
    lista3.append(lista1[x])
    lista3.append(lista2[x])

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print(f'Lista 3: {lista3}')