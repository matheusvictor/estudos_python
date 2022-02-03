def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome.capitalize()} fez {gols} gol(s) no campeonato.')


nome_jogador = str(input('Nome do jogador: '))
qtd_gols = input('Número de gols: ')

if qtd_gols.isnumeric():
    qtd_gols = int(qtd_gols)
else:
    qtd_gols = 0
if nome_jogador.strip() == '':
    ficha(gols=qtd_gols)
else:
    ficha(nome_jogador, qtd_gols)
