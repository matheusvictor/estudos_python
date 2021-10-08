from random import randint
numero_gerado = randint(0, 5)
numero_digitado = int(input("Digite um número: "))
print(f'O número gerado foi {numero_gerado}. Você digitou o número {numero_digitado}.')
if numero_digitado == numero_gerado:
    print("Você acertou!")
else:
    print("Você errou!")
