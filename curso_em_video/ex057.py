continua = True
while(continua):
    sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()
    if('M' in sexo or 'F' in sexo):
        continua = False
    else:
        print('Entrada inválida. Tente novamente!', end=' ')

print('Registrado com sucesso!')
