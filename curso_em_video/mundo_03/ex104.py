def leiaInt(msg):
    isNotANumber = True

    while isNotANumber:
        msg = input('Erro! Digite um número inteiro: ')

        if msg.isnumeric():
            msg = int(msg)
            isNotANumber = False
            break

    return msg


numero = leiaInt(input('Digite um número inteiro: '))
print(f'Você acabou de digitar o número {numero}!')
