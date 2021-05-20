"""
3. Classe Retangulo: Crie uma classe que modele um retangulo:
a.Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
b.Metodos: Mudar valor dos lados, Retornar valor dos lados, calcular Area e calcular Perimetro;
c.Crie um programa que utilize esta classe. Ele deve pedir ao usuario que informe as medidades de um local. 
Depois, deve criar um objeto com as medidas e calcular a
quantidade de pisos e de rodapes necessarias para o local.
"""
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def mudaBase (self, base):
        self.base = base

    def mudaAltura (self, altura):
        self.altura = altura

    def retornaBase (self):
        return self.base
    
    def retornaAltura (self):
        return self.altura

    def area (self):
        return self.base * self.altura
    
    def perimetro (self):
        return (self.base*2) + (self.altura*2)

#Input para definir a base b e a altura h
b = float(input("Informe o comprimento do local: "))
h = float(input("Informe a largura do local: "))

#Criando objeto retangulo
ret = Retangulo(b, h)

#Utilizando o método para calcular area e informar a quantidade de pisos
print("Quantidade de pisos necessária (em m2): ", ret.area())

#Utilizando metodo para calcular perimetro e informar quantidade de rodape
print("Quantidade de rodape necessária (em m): ", ret.perimetro())