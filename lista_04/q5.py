# -*- coding: utf-8 -*-

distancia = input("Digite a distância, em km, a ser percorrida: ")
consumoMedio = input("Digite o consumo médio do veículo: ")

litrosNecessario = distancia * consumoMedio

print("\nSão necessário, no mínimo, {0}L de combustível para percorrer essa distância.".format(litrosNecessario))