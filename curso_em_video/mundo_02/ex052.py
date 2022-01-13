numero = int(input('Digite um número inteiro para saber se ele é primo: '))
numero_divisores = 0

for contador in range(1, numero+1):
    if (numero % contador == 0):
        print('\033[33m', end='')
        numero_divisores += 1
    print(f'{contador}\033[m', end=' ')

print(f'\nO número {numero} foi dividido {numero_divisores} vez(es).')

if(numero_divisores == 2):
    print('Por isso, ele \033[34mé\033[m um número primo!')
else:
    print('Por isso, ele \033[31mnão é\033[m um número primo!')
