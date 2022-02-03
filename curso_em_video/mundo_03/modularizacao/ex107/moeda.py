def aumentar(valor, porcentagem=10):
    novo_valor = valor + valor * (porcentagem / 100)
    return novo_valor


def diminuir(valor, porcentagem=10):
    novo_valor = valor - valor * (porcentagem / 100)
    return novo_valor


def dobro(valor):
    dobro_valor = valor * 2
    return dobro_valor


def metade(valor):
    metade_valor = valor / 2
    return metade_valor
