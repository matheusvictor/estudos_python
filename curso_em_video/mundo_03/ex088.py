from random import randint


def gera_jogos():
    jogos_gerados = list()
    quantidade_jogos = int(input('Quantos jogos você deseja gerar? Resp.: '))
    lista_temporaria = []
    contador = 0

    while contador < quantidade_jogos:
        for i in range(0, 6):
            numero_aleatorio = randint(1, 60)
            if numero_aleatorio not in lista_temporaria:
                lista_temporaria.append(numero_aleatorio)
            else:
                numero_aleatorio = randint(1, 60)
                lista_temporaria.append(numero_aleatorio)
        jogos_gerados.append(lista_temporaria[:])
        lista_temporaria.clear()
        contador += 1

    return jogos_gerados


def imprime_jogos_gerados(lista_jogos):
    for jogo in range(len(lista_jogos)):
        lista_jogos[jogo].sort()
        print(f'{jogo + 1}º jogo: {lista_jogos[jogo]}')


imprime_jogos_gerados(gera_jogos())
