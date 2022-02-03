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
