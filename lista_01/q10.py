# -*- coding: utf-8 -*-

while(True):
    print("Informe o tipo de valor que deseja inserir em A:")
    print("1 - Número (inteiros ou reais)")
    print("2 - Caracter(es)")
    opc = int(input())

    if(opc == 1):
        a = input("\nInforme o valor de A: ")
        break
    elif(opc == 2):
        a = raw_input("\nInforme o valor de A: ")
        break

while(True):
    print("\nInforme o tipo de valor que deseja inserir em B:")
    print("1 - Número (inteiros ou reais)")
    print("2 - Caracter(es)")
    opc = int(input())

    if(opc == 1):
        b = input("\nInforme o valor de B: ")
        break
    elif(opc == 2):
        b = raw_input("\nInforme o valor de B: ")
        break

# verifica os atuais valores atribuídos às variáveis 'a' e 'b'
print(a, b)
# A variável 'aux' irá guardar o antigo valor de 'a'
aux = a
# 'a' receberá o valor de 'b'. Neste caso, o valor recebido por 'a' será 20
a = b
# 'b' irá receber o antigo valor de 'a', que foi guardado na varivável 'aux'
b = aux
# verifica se os valores de 'a' e 'b' foram trocados
print(a, b)