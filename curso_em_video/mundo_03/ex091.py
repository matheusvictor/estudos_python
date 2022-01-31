from random import randint
from operator import itemgetter
from time import sleep

lista_jogadores = dict()
maior_pontuacao = 0
contador_jogadores = 1

numero_jogadores = int(input('Digite o número de jogadores: '))

for i in range(numero_jogadores):
    lista_jogadores[f'jogador_{contador_jogadores}'] = randint(1, 6)
    contador_jogadores += 1

ranking = sorted(lista_jogadores.items(), key=itemgetter(1), reverse=True)

print(' ===== RANKING DOS JOGADORES ===== ')
for posicao, jogador in enumerate(ranking):
    sleep(1)
    print(f' {posicao + 1}º lugar: {jogador[0]} com {jogador[1]} pontos.')
