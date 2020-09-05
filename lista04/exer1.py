#Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor 
#valor, sem usar as funções max e min.
from random import randint

lista = []
for x in range (10):
    n = randint(1, 100)
    lista.append(n)

print(f'A lista sorteada foi: {lista}')

lista.sort()
maior = lista[-1]
menor = lista[0]

print(f'O menor número da lista é {menor} e o maior é {maior}')
