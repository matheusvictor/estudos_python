soma = 0
for contador in range(0, 6):
    numero = int(input(f'Digite o {contador+1}º número: '))
    if(numero % 2 == 0):
        soma += numero
print(f'A soma dos números pares digitados é igual a: {soma}')
