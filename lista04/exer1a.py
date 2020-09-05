#Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor 
#valor, sem usar as funções max e min.
from random import sample

lista = sample(range(100), 10)
print(f'A lista sorteada foi: {lista}')

maior = menor = lista[0]
n = 1
while n < 10:
    if lista[n] > maior:
        maior = lista[n]
    if lista[n] < menor:
        menor = lista[n]
    n += 1
print(f'O menor número da lista é {menor} e o maior é {maior}')
