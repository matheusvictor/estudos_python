# -*- coding: utf-8 -*-

while(True):
    numero = input("Digite uma nota entre 0 e 10: ")

    if(numero > 10 or numero < 0):
        print("A nota deve ser entre 0 e 10!\n ")
    else:
        print("\nNota: {0}".format(numero))
        break