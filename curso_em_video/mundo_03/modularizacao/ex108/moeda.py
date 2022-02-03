def aumentar(valor=0, porcentagem=10):
    novo_valor = valor + valor * (porcentagem / 100)
    return novo_valor


def diminuir(valor=0, porcentagem=10):
    novo_valor = valor - valor * (porcentagem / 100)
    return novo_valor


def dobro(valor=0):
    dobro_valor = valor * 2
    return dobro_valor


def metade(valor=0):
    metade_valor = valor / 2
    return metade_valor


def formata_moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
