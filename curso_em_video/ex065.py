numero = soma = media = maior = menor = contador = 0
lista_numeros = []
continua = True

while(continua):
    numero = int(input('Digite um número: '))
    lista_numeros.append(numero)
    contador += 1
    opcao_continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    if('N' in opcao_continuar):
        continua = False
        soma = sum(lista_numeros)
        media = soma / len(lista_numeros)
        maior = max(lista_numeros)
        menor = min(lista_numeros)

print(f'\nForam lidos {contador} números. Sendo {maior} o maior número e {menor} o menor entre eles.\n'
      f'A soma entre eles é igual a {soma}.'
      f'\nA média equivale a {media:.2f}')
