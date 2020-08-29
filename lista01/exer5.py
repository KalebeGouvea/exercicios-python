#Solicite o preço de uma mercadoria e o percentual de desconto. 
#Exiba o valor do desconto e o preço a pagar.

preco = float(input('Digite o preço da mercadoria: '))
desc = float(input('Digite o percentual de desconto (em %): '))/100
vdesc = preco * desc
pdesc = preco - vdesc

print (f'O valor do desconto foi R$ {vdesc:.2f}')
print (f'O preço a pagar é R$ {pdesc:.2f}')