soma = 0
for numero in range(1,501,2):
    if(numero % 3 == 0):
        soma += numero
print(f'A soma dos números ímpares e múltiplos de três entre 1 e 500 é igual a: {soma}')
