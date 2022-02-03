def aumentar(valor=0, porcentagem=10, formata=False):
    novo_valor = valor + valor * (porcentagem / 100)
    if formata:
        return formata_moeda(novo_valor)
    else:
        return novo_valor


def diminuir(valor=0, porcentagem=10, formata=False):
    novo_valor = valor - valor * (porcentagem / 100)
    return novo_valor if formata is False else formata_moeda(novo_valor)


def dobro(valor=0.0, formata=False):
    dobro_valor = valor * 2
    return dobro_valor if formata is False else formata_moeda(dobro_valor)


def metade(valor=0.0, formata=False):
    metade_valor = valor / 2.0
    return metade_valor if not formata else formata_moeda(metade_valor)


def formata_moeda(valor=0.0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, aumento=0, reducao=0):
    print('-' * 30)
    print('RESUMO'.center(30))
    print('-' * 30)
    print(f'Valor analisado: {formata_moeda(valor)}')
    print(f'Dobro do valor: {dobro(valor, True)}')
    print(f'Metade do valor: {metade(valor, True)}')
    print(f'{aumento}% de aumento: {aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: {diminuir(valor, reducao, True)}')

