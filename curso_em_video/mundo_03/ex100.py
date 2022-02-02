from random import randint
from time import sleep


def sorteia(lista_numeros):
    print('Sorteando 5 valores entre 0 e 10: ', end='')
    for contador in range(0, 5):
        numero_aleatorio = randint(0, 10)
        print(numero_aleatorio, end=' ')
        sleep(0.3)
        lista_numeros.append(numero_aleatorio)
    print('>> PRONTO!')

    return lista_numeros


def soma_pares(lista_numeros):
    soma_pares = 0
    quantidade_pares = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            soma_pares += numero
            quantidade_pares += 1

    print(f'Entre os números {lista_numeros}, {quantidade_pares} são pares e a soma deles é igual a {soma_pares}!')


numeros = list()
soma_pares(sorteia(numeros))
