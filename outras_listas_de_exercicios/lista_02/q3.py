# -*- coding: utf-8 -*-

n1, n2 = 0, 0

for i in range(1, 3):
    nota = input("Digite a {0}ª nota: ".format(i))

    if(i == 1):
        n1 = nota
    if(i == 2):
        n2 = nota

media = (n1 + n2) / 2

if(media >= 6):
    print("\nAprovado com média {0}".format(media))
else:
    print("\nReprovado com média {0}".format(media))