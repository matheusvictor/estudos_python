def ficha(nome='', gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = int('0')

    print(f'O jogador {nome.capitalize()} fez {gols} gols no campeonato.')


nome_jogador = str(input('Nome do jogador: '))
qtd_gols = input('Gols: ')
ficha(nome_jogador, qtd_gols)
