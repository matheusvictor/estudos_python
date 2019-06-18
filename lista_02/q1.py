# -*- coding: utf-8 -*-

a = input("Digite o primeiro valor: ")

maior = a
menor = a

while(True):
    b = input("Digite o segundo valor: ")

    if(a != b):
        if(b > a):
            maior = b
        elif(b < a):
            menor = b
        break
    else:
        print "O segundo valor não pode ser igual ao primeiro."

while(True):
    c = input("Digite o terceiro valor: ")

    if(c != a and c != b):
        if(c > a and c > b):
            maior = c
        elif(c < a and c < b):
            menor = c
        break
    else:
        print "O terceiro valor não pode ser igual ao primeiro nem ao segundo valor."

print("\nEntre os números digitados, {0} é o maior e {1} é o menor.".format(maior, menor))