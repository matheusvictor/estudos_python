# -*- coding: utf-8 -*-

fahrenheit = float(input("Digite a temperatura em ºF a ser convertida para ºC: "))

celsius = ((fahrenheit - 32) * 5) / 9 

print("{0}ºF é igual a {1}ºC".format(fahrenheit, celsius))