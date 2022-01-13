primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

if(primeiro_numero > segundo_numero):
    print('O primeiro número é o maior!')
elif(segundo_numero > primeiro_numero):
    print('O segundo número é o maior!')
else:
    print('Não existe número maior, pois eles são iguais!')
