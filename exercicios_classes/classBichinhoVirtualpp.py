# -*- coding: utf-8 -*-
"""
15. Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, 
permitindo que o usuário especifique quanto de comida ele fornece 
ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com 
que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

16. Crie uma "porta escondida" no programa do programa do bichinho virtual 
que mostre os valores exatos dos atributos do objeto. Consiga isto mostrando 
o objeto quando uma opção secreta, não listada no menu, for informada na 
escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.

17. Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo 
o controle deles através de uma lista. Imite o funcionamento do programa básico, 
mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que 
ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário 
executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar 
com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais 
interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.
"""
class Tamagushi:
    def __init__(self, nome, idade, fome, saude):
        self.mudarNome(nome)
        self.mudarIdade(idade)
        #Atributo fome: maior é melhor
        self.mudarFome(fome)
        #Atributo saúde: maior é melhor
        self.mudarSaude(saude)
    
    def mudarNome(self, nome):
        self.nome = nome

    def mudarIdade(self, idade):
        self.idade = idade

    def mudarFome(self, fome):
        self.fome = fome
    
    def mudarSaude(self, saude):
        self.saude = saude
    
    def alimentar(self, qtd):
        self.mudarFome(self.obterFome() + qtd)
    
    def brincar(self, tempo):
        self.mudarSaude(self.obterSaude() + tempo)

    def obterNome(self):
        return self.nome
    
    def obterIdade(self):
        return self.idade
    
    def obterFome(self):
        return self.fome
    
    def obterSaude(self):
        return self.saude
    
    def obterHumor(self):
        return self.obterSaude() * self.obterFome()

    def str(self):
        return "Nome: " + str(self.obterNome()) + " Idade: " + str(self.obterIdade()) + " Fome: " + str(self.obterFome()) + " Saúde: " + str(self.obterSaude()) + " Humor: " + str(self.obterHumor())

#Criando objeto bichinho
bichinho = Tamagushi("Horácio", 0, 80, 80)

#Print que testa o retorno dos métodos
print(bichinho.obterNome(), bichinho.obterIdade(), bichinho.obterFome(), bichinho.obterSaude(), bichinho.obterHumor())

#Utilizando métodos alimentar e brincar e exibindo os resultados com print
bichinho.alimentar(10)
bichinho.brincar(10)
print(bichinho.obterNome(), bichinho.obterIdade(), bichinho.obterFome(), bichinho.obterSaude(), bichinho.obterHumor())

#Utilizando o método especial str
print(bichinho.str())