# -*- coding: utf-8 -*-

nome = raw_input("Digite o nome do(a) aluno(a):\n")

# as notas recebidas pelo usuário serão logo multiplicadas pelo seus respectivos pesos
n1 = float(input("Digite a 1ª nota:\n") * 2) 
n2 = float(input("Digite a 2ª nota:\n") * 3)
n3 = float(input("Digite a 3ª nota:\n") * 5)

mediaFinal = (n1 + n2 + n3)/10

print("A média de {0} é: {1}".format(nome, mediaFinal))