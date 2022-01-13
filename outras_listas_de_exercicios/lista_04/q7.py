# -*- coding: utf-8 -*-

litrosVendidos = input("Litro(s) vendido(s): ")

while(True):
    tipoCombustivel = int(input("Digite o tipo do combustível:\n1 - Álcool\n2 - Gasolina\nCód.: "))

    if(tipoCombustivel == 1 or tipoCombustivel == 2):
        break

precoAlcool = 3.90
precoGasolina = 4.30

if(tipoCombustivel == 1):
    if(litrosVendidos <= 20):
        desconto = 0.03
        precoNormal = litrosVendidos * precoAlcool
        litrosDesconto = precoNormal * desconto
        totalPagar = precoNormal - litrosDesconto
    else:
        desconto = 0.05
        precoNormal = litrosVendidos * precoAlcool
        litrosDesconto = precoNormal * desconto
        totalPagar = precoNormal - litrosDesconto   

    print("\nLitros vendidos: {0}L\nTipo de combustível: Álcool\nPreço por litro: R$ {1}\nTotal: R${2}\nDesconto: R${3} ({4}%)\nTotal a pagar: R${5}".format(litrosVendidos, precoAlcool, precoNormal, litrosDesconto, desconto, totalPagar))

if(tipoCombustivel == 2):
    if(litrosVendidos <= 20):
        desconto = 0.04
        precoNormal = litrosVendidos * precoGasolina
        litrosDesconto = precoNormal * desconto
        totalPagar = precoNormal - litrosDesconto
    else:
        desconto = 0.06
        precoNormal = litrosVendidos * precoGasolina
        litrosDesconto = precoNormal * desconto
        totalPagar = precoNormal - litrosDesconto

    print("\nLitros vendidos: {0}L\nTipo de combustível: Gasolina\nPreço por litro: R$ {1}\nTotal: R${2}\nDesconto: R${3} ({4}%)\nTotal a pagar: R${5}".format(litrosVendidos, precoGasolina, precoNormal, litrosDesconto, desconto, totalPagar))
