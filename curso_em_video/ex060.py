numero = float(input('Digite um número qualquer para saber seu fatorial: '))
contador = numero
fatorial = numero

while(contador > 1):
    contador -= 1
    fatorial *= (contador)
    print(contador)

print(fatorial)
