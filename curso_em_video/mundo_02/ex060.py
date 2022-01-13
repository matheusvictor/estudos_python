numero = int(input('Digite um número qualquer para saber seu fatorial: '))
contador = numero
fatorial = 1 #inicia variável com fator nulo da multiplicação

while(contador > 0):
    print(contador, end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= (contador) #na 1ª vez do lado, fatorial passará a ser o numero digitado, pois 1 * n = n
    contador -= 1

print(f'{numero}! = {fatorial}')
