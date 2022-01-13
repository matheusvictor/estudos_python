lista_numeros = [[], []]

for valor in range(0, 6):
    numero = int(input('Digite um número: '))

    if(numero % 2 == 0):
        lista_numeros[0].insert(valor, numero)
    else:
        lista_numeros[1].insert(valor, numero)

print(f'Os valores pares digitados foram: {lista_numeros[0][:]}')
print(f'Os valores ímpares digitados foram: {lista_numeros[1][:]}')
