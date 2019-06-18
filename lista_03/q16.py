# -*- coding: utf-8 -*-

limite = int(input("Digite a qtd de números a ser verificada se é ou não um número primo:\n"))

# O zero não será considerado. Por isso, precisamos utilizar (limite+1) para que a contagem
# seja feita de 1 até o número digitado pelo usuário
for i in range(1, (limite+1)):

    # O indentificador 'dividores' irá guardar a quantidade de divisões realizadas
    # e será zerado toda vez que o laço abaixo terminar sua verificação e retornar
    # ao topo para realizar uma nova busca com o novo valor de i.
    divisores = 0

    # Verifica todas as combinações entre j e i 
    # Ex.: j = 1 e i = 1, j = 1 e i = 2, j = 1 e i = n
    for j in range(1, (i+1)):

        # Se o resto da divisão da posição de i por j for igual a zero, o indentificador
        # 'dividores' registratá a ocorrência.
        # Ex.: i = 1 e j = 1. 
        if(i % j == 0):
            divisores += 1
    
    # Se houverem mais de dois divisores para este número ele não é primo,
    # pois, um número primo só tem dois divisores: 1 e ele mesmo.
    if(divisores > 2):
        print('{0} não é um número primo!'.format(i))
    else:
        print('{0} é um número primo!'.format(i))