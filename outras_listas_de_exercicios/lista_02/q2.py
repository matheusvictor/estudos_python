# -*- coding: utf-8 -*-

a = input("Digite o primeiro valor: ")

while(True):
    b = input("Digite o segundo valor: ")

    if(a != b):
        break
    else:
        print "O segundo valor não pode ser igual ao primeiro."

while(True):
    c = input("Digite o terceiro valor: ")

    if(c != a and c != b):
        break
    else:
        print "O terceiro valor não pode ser igual ao primeiro nem ao segundo valor."

if(a < b and a < c):
    soma = b + c
elif(b < a and b < c):
    soma = a + c
else:
    soma = a + b

print("\nA soma entre os dois maiores números digitados é igual a {0}.".format(soma))