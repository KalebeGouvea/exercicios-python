#A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... 
#Sua regra de formação é simples: os dois primeiros elementos são 1; a partir 
#de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que 
#leia um número inteiro calcule o seu número de Fibonacci. 
#F1 = 1, F2 = 1, F3 = 2, etc.

fn = int(input('Digite um número inteiro: '))

x = 3
f = [1,1]
while x <= fn:
    n = f[-1] + f[-2]
    f.append(n)
    x += 1
print(f'O seu número de Fibonacci é {f[-1]}')