#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha 
#igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as 
#informações.

user = input('Digite um usuário: ')
pwd = input('Digite uma senha: ')
while user == pwd:
    print('Usuário e senha não podem ser iguais')
    user = input('Digite um usuário: ')
    pwd = input('Digite uma senha: ')
print('OK')