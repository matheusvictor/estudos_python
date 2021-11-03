lista_valores = list()
continua = True

while(continua):
    valor = int(input('Digite um valor a ser armanezado: '))

    if not valor in lista_valores:
        lista_valores.append(valor)
    else:
        print('Valor não adicionado! Motivo: duplicado.')

    opc = input('Deseja continuar inserindo valores? [S/N]: ').strip().upper()[0]

    if 'N' in opc:
        continua = False

lista_valores.sort()
print(f'Os números digitados em ordem crescente foram: {lista_valores}')
