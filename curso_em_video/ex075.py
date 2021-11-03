from random import randint

# armazenando 4 números digitados em uma tupla
numeros = tuple(int(input(f'Digite o {c}º número: ')) for c in range(1, 5))

print(f'O número 9 apareceu na tupla {numeros.count(9)} ', end='')

if numeros.count(9) == 1:
    print('vez.')
else:
    print('vezes.')

if(3 in numeros):
    print(f'O número 3 apareceu pela primeira vez na posição {numeros.index(3)+1}.')

print('Os números pares foram: ', end='')
# para cada número presente no conjunto de números...
for numero in numeros:
    if(numero % 2 == 0 and numero != numeros[-1]):
        print(numero, end=' ')
