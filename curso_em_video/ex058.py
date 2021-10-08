from random import randint
numero_gerado = randint(0, 10)
continua = True
tentativas = 1

while(continua):
    numero_digitado = int(input("Digite um número: "))

    if(numero_digitado == numero_gerado):
        continua = False
    else:
        tentativas += 1

print(f'O número gerado foi {numero_gerado}. Você acertou com {tentativas} tentativa(s)!')
