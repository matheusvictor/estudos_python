nome_jogador = str(input('Nome do jogador: '))
partidas_jogadas = int(input(f'Quantas partidas foram jogadas por {nome_jogador}?: '))

quantidade_gols_partida = list()
total_gols = 0

for partida in range(partidas_jogadas):
    quantidade_gols_partida.append(int(input(f'Quantidade de gols feitos na {partida + 1}ª partida: ')))
    total_gols += quantidade_gols_partida[partida]

estatisticas_jogador = {'nome': nome_jogador, 'partidas_jogadas': partidas_jogadas,
                        'gols_por_partida': quantidade_gols_partida, 'total_gols': total_gols}

print('-=' * 20)
for k, v in estatisticas_jogador.items():
    print(f'{k}: {v}')
print('-=' * 20)
print(f'O jogador {estatisticas_jogador["nome"]} jogou {estatisticas_jogador["partidas_jogadas"]} partida(s).')
for i, v in enumerate(estatisticas_jogador['gols_por_partida']):
    print(f'Na {i + 1}ª partida fez {v} gol(s)')
print(f'Foi um total de {estatisticas_jogador["total_gols"]} gol(s)!')
print('-=' * 20)
