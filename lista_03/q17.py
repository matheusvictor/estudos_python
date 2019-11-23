# -*- coding: utf-8 -*-

saque = int(input("Digite o valor que deseja sacar: R$ "))
resto = saque
notaCem, notaCinq, notaVinte, notaDez, notaCinco, notaDois, notaUm  = 0, 0, 0, 0, 0, 0, 0

if(resto >= 100):
    notaCem = resto / 100
    resto = resto % 100

if(resto >= 50):
    notaCinq = resto / 50
    resto = resto % 50

if(resto >= 20):
    notaVinte = resto / 20
    resto = resto % 20

if(resto >= 10):
    notaDez = resto / 10
    resto = resto % 10

# verifica se o número é ímpar
if(resto % 2 != 0):
    # caso seja ímpar, verifica se o valor é divisível por 5
    if(resto >= 5):
        notaCinco = resto / 5
        resto = resto % 5
    # caso seja par, verifica se o valor é divisível por 2
    elif(resto >= 2):
        notaDois = resto / 2
        resto = resto % 2

if(resto >= 1):
    print "Este valor não é sacável, pois necessitaria de, pelo menos, uma nota de R$1."
else:
    print "\nValor sacado: R$", saque, "\nSaída:\n", notaCem, "nota(s) de R$ 100", "\n", notaCinq, "nota(s) de R$ 50", "\n", notaVinte, "nota(s) de R$ 20", "\n", notaDez, "nota(s) de R$ 10", "\n", notaCinco, "nota(s) de R$ 5", "\n", notaDois, "nota(s) de R$ 2"