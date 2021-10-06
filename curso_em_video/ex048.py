soma = 0
contador = 0
for numero in range(1,501,2):
    if(numero % 3 == 0):
        soma += numero
        contador += 1
print(f'Existem {contador} números, entre 1 e 500, que são ímpares e múltiplos de 3. A soma entre eles é igual a: {soma}.')
