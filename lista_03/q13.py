i = 1
numero = float(input("Digite um numero:\n"))

maior = numero
menor = numero

for i in range(i, 10):
    numero2 = float(input("Digite um numero:\n"))

    if(numero2 > maior):
        maior = numero2
    if(numero2 < menor):
        menor = numero2

print(maior, menor)