# -*- coding: utf-8 -*-

valorTotal = 0
quantidade = 0

while(True):
    preco = input("Digite o valor da mercadoria: R$")
    continua = int(input("Digite 1 para continuar ou 2 para sair: "))

    valorTotal = valorTotal + preco
    quantidade += 1

    while(continua < 1 or continua > 2):
        continua = int(input("\nValor inválido! Digite 1 para continuar ou 2 para sair: "))
    
    if(continua == 2):
        break

mediaPreco = valorTotal / quantidade
print("\nQuantidade de produtos: {0}\nValor total: R${1}\nMédia de preço: R${2}".format(quantidade, valorTotal, mediaPreco))