# -*- coding: utf-8 -*-

while(True):
    nome = raw_input("Digite o nome: ")
    if(len(nome) >= 3):
        break

while(True):
    idade = int(input("Digite a idade: "))
    if(idade > 0 and idade < 150):
        break

while(True):        
    sexo = raw_input("Sexo: ").upper()
    # armazenando apenas a primeira letra digitada:
    charSexo = sexo[0]
    if(charSexo != 'F' and charSexo != 'M'):
        print("Informação inválida!")
    else:
        break

while(True):        
    estadoCivil = raw_input("Estado civil: ").upper()
    # armazenando apenas a primeira letra digitada:
    charEstadoCivil = estadoCivil[0]
    if(charEstadoCivil != 'S' and charEstadoCivil != 'C' and charEstadoCivil != 'V' and charEstadoCivil != 'D'):
        print("Informação inválida!")
    else:
        break

while(True):
    salario = input("Informe o salário: R$")
    if(salario < 0):
        print("Informação inválida!")
    else:
        break

print("\nNome: {0}\nIdade: {1}\nSexo: {2}\nEstado Civil: {3}\nSalário: R${4}".format(nome, idade, charSexo, charEstadoCivil, salario))