def maior(*valores):
    maior = 0
    lista_valores = list()
    lista_valores.append(valores)
    quantidade_valores = len(lista_valores[0])

    print('-=' * 30)

    if len(lista_valores[0]) > 1:
        print('Foram informados os valores: ', end='')
        for numero in lista_valores[0]:
            print(numero, end=' ')
            if numero > maior:
                maior = numero
        print()
        print(f'Ao todo são {quantidade_valores} números e o maior dentre eles é o {maior}!')

    elif len(lista_valores[0]) == 1:
        print(f'Foi informado apenas o número {lista_valores[0][0]}, sendo ele próprio o maior!')
    else:
        print('Não foram passados parâmetros!')
    return 0


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
maior()
