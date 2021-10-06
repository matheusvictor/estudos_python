numero = int(input('Digite um número inteiro para saber se ele é primo: '))

numero_divisores = 0
for contador in range(1, numero+1):
    if (numero % contador == 0):
        numero_divisores +=1

if(numero_divisores > 2):
    print(f'O número {numero} não é primo!')
else:
    print(f'O número {numero} é primo!')
