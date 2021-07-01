"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
a.Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
i.tipoCombustivel.
ii.valorLitro
iii.quantidadeCombustivel

b.Possua no mínimo esses métodos:
i.abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra 
a quantidade de litros que foi colocada no veículo
ii.abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível 
e mostra o valor a ser pago pelo cliente.
iii.alterarValor( ) – altera o valor do litro do combustível.
iv.alterarCombustivel( ) – altera o tipo do combustível.
v.alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""

class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.alterarCombustivel(tipoCombustivel)
        self.alterarValor(valorLitro)
        self.alterarQuantidadeCombustivel(quantidadeCombustivel)
    
    def abastecerPorValor(self, valor):
        diferenca = self.quantidadeCombustivel - valor/self.valorLitro
        if diferenca >= 0:
            self.alterarQuantidadeCombustivel(diferenca)
            #Quantidade de litros colocada no veículo:
            return valor/self.valorLitro
        

    def abastecerPorLitro(self, litros):
        diferenca = self.quantidadeCombustivel - litros
        if diferenca >= 0:
            self.alterarQuantidadeCombustivel(diferenca)
            #Valor a ser pago pelo cliente:
            return litros*self.valorLitro

    def alterarValor(self, valor):
        self.valorLitro = valor

    def alterarCombustivel(self, tipo):
        self.tipoCombustivel = tipo

    def alterarQuantidadeCombustivel(self, qtd):
        self.quantidadeCombustivel = qtd

bomba = bombaCombustivel("gasolina", 6.10, 100)

print(vars(bomba))
print("Qtd. de litros colocada no veículo: ", bomba.abastecerPorValor(50))
print(vars(bomba))

print("Valor a ser pago: ", bomba.abastecerPorLitro(80))
print(vars(bomba))

bomba.alterarValor(5.95)
bomba.alterarCombustivel("diesel")
bomba.alterarQuantidadeCombustivel(50)
print(vars(bomba))