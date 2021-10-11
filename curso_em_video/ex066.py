numero = soma = contador = 0

while(numero != 999):
    numero = int(input('Digite um número (insira 999 se quiser parar o programa): '))

    if(numero != 999):
        soma += numero
        contador += 1
    else:
        break

print(f'Você digitou {contador} números e a soma entre eles é igual a {soma}!')
print('Programa encerrado!')
