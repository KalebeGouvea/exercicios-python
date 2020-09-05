#Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista 
#PAR e os números ímpares na lista IMPAR. Imprima as três listas.

from random import sample

lista = sample(range(100), 20)
print(f'A lista sorteada foi: {lista}')

par = []
impar = []
n = 0
while n < 20:
    if lista[n] % 2 == 0:
        par.append(lista[n])
    else:
        impar.append(lista[n])
    n += 1
print(f'A lista par foi: {par}')
print(f'A lista impar foi: {impar}')
