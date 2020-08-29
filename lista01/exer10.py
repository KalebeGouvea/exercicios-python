#Escreva um programa para calcular a redução do tempo de vida de um fumante. 
#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
#Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule 
#quantos dias de vida um fumante perderá. Exiba o total de dias.

qtd_dia = int(input('Quantos cigarros fuma por dia? '))
qtd_anos = int(input('Por quantos anos fumou? '))
total_min = qtd_dia * 10 * qtd_anos*365
total_dias = total_min/1440

print(f'Foram perdidos {total_dias:.1f} dias de vida.')