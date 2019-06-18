# -*- coding: utf-8 -*-

anoAtual = int(input("Digite o ano atual: "))
anoNasc = int(input("Digite o ano de seu nascimento: "))

idade = anoAtual - anoNasc

if(idade >= 16):
    print("\nVocê não poderá votar este ano.")
else:
    print("\nVocê poderá votar este ano.")