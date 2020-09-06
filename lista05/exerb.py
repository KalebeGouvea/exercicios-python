#Questão B. Quantas vezes o trecho de pseudocódigo seguinte imprime 'oi'? 
#(obs: na nossa pseudo-linguagem, o laço inclui os extremos, ou seja, 1 até 4 
#significa 1, 2, 3, 4.)
n = 0
for i in range(1,10):
    if i != 3:
        for j in range(1,7):
            print('oi')
            n += 1
print(n)