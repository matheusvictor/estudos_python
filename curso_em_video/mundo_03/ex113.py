def leiaInt(msg):
    isNotANumber = True
    while isNotANumber:
        try:
            msg = int(input(f'{msg} '))
        except (ValueError, TypeError):
            print('Erro! Digite um número inteiro válido!')
            continue
        except KeyboardInterrupt:
            return'\nEntrada de dados interrompida pelo usuário!'
            break
        else:
            isNotANumber = False
            return msg


def leiaFloat(msg):
    isNotANumber = True
    while isNotANumber:
        try:
            msg = float(input(f'{msg} '))
        except (ValueError, TypeError):
            print('Erro! Digite um número inteiro válido!')
            continue
        except KeyboardInterrupt:
            return'\nEntrada de dados interrompida pelo usuário!'
            break
        else:
            isNotANumber = False
            return msg


entrada = leiaInt('Digite um número inteiro:')
if entrada:
    print(f'Você acabou de digitar o número {entrada}!')
else:
    print(entrada)

nova_entrada = leiaFloat('Digite um número real:')
if entrada:
    print(f'Você acabou de digitar o número {nova_entrada}!')
else:
    print(nova_entrada)
