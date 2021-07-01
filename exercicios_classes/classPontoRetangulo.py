"""
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
a. Possua uma classe chamada Ponto, com os atributos x e y.
b. Possua uma classe chamada Retangulo, com os atributos largura e altura.
c. Possua uma função para imprimir os valores da classe Ponto
d. Possua uma função para encontrar o centro de um Retângulo.
e. Você deve criar alguns objetos da classe Retangulo.
f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior 
esquerdo do retângulo, que deve ser um objeto da classe Ponto.
g. A função para encontrar o centro do retângulo deve retornar o valor para um 
objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
h.O valor do centro do objeto deve ser mostrado na tela.
i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

def printPonto(ponto):
    print("Coordenada x: ", ponto.x)
    print("Coordenada y: ", ponto.y)

def centro(retangulo):
    print("Coordenada x: ", retangulo.largura/2)
    print("Coordenada y: ", retangulo.altura/2)