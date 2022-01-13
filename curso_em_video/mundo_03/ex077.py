lista_palavras = ('casa', 'boneca', 'futebol', 'programar', 'codigo', 'arara azul')

for palavra in lista_palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    vogais = 0
    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogais += 1
            print(f'{letra}', end=' ')
    print(f'. Ao todo são {vogais} vogais.')
