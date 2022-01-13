lista_valores = list()
lista_pares = list()
lista_impares = list()
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

for numero in lista_valores:
    if(numero % 2 == 0):
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f'Foram digitados {len(lista_valores)} números. Os números digitados foram: {lista_valores}')
print(f'Dentre eles, são números pares: {lista_pares}')
print(f'Dentre eles, são números ímpares: {lista_impares}')
