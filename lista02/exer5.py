#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print (f'O maior número é {maior}')
print (f'O menor número é {menor}')

"""Ou também
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 >= n2 and n1 >= n3:
    print (f'O maior número é {n1}')
elif n2 >= n3:
    print (f'O maior número é {n2}')
else:
    print (f'O maior número é {n3}')

if n1 <= n2 and n1 <= n3:
    print (f'O menor número é {n1}')
elif n2 <= n3:
    print (f'O menor número é {n2}')
else:
    print (f'O menor número é {n3}')
"""