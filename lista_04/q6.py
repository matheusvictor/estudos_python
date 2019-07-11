# -*- coding: utf-8 -*-
custoFabrica = input("Digite o valor do custo de fábrica do PC: R$")

imposto = 0.47
frete = 0.13

pcImpostos = custoFabrica * imposto
pcFrete = pcImpostos * frete

custoFinal = custoFabrica + pcImpostos + pcFrete
print(frete)

print("\nCusto de fábrica: {0}\nImpostos: R${1}\nFrete: R${2}\nCusto final: R${3}".format(custoFabrica, pcImpostos, pcFrete, custoFinal))