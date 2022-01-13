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

lista_valores.sort(reverse=True)

print(f'Foram digitados {len(lista_valores)} números. Os números digitados em ordem decrescente foram: {lista_valores}')

if 5 in lista_valores:
    print(f'O número 5 encontra-se entre os valores, mais precisamente na {lista_valores.index(5) + 1}ª posição.')
else:
    print('O número 5 não se encontra entre os valores digitados.')
