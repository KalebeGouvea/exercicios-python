#Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é 
#sortudo se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, 
#quantos números sortudos existem entre 18644 e 33087, incluindo os extremos?

n = 0
for x in range(18644, 33088):
    y = str(x)
    if '2' in y and '7' not in y:
        n += 1

print(n)