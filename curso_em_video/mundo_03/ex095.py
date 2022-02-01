lista_jogadores = list()

continua = True
while continua:

    nome_jogador = str(input('Nome do jogador: '))
    partidas_jogadas = int(input(f'Quantas partidas foram jogadas por {nome_jogador}?: '))

    quantidade_gols_partida = list()
    total_gols = 0

    for partida in range(partidas_jogadas):
        quantidade_gols_partida.append(int(input(f'Quantidade de gols feitos na {partida + 1}ª partida: ')))
        total_gols += quantidade_gols_partida[partida]

    estatisticas_jogador = {'nome': nome_jogador, 'partidas_jogadas': partidas_jogadas,
                            'gols_por_partida': quantidade_gols_partida, 'total_gols': total_gols}

    lista_jogadores.append(estatisticas_jogador.copy())
    estatisticas_jogador.clear()

    resposta = str(input('Deseja continuar? [S/N]: '))

    while resposta not in 'SsNn':
        resposta = str(input('Opção inválida! Tente novamente [S/N]: ')).upper()[0]

    if resposta in 'Nn':
        continua = False
        break

print('-=' * 40)
print(f'{"COD":<10}{"NOME":<10}{"GOLS":<10}{"TOTAL":<10}')
print('-' * 40)
for index, jogador in enumerate(lista_jogadores):
    print(f'{index:<5}{"":<5}{jogador["nome"]}{"":<10}{jogador["gols_por_partida"]}{"":<10}{jogador["total_gols"]}')
print('-' * 40)

while True:

    opcao = int(input('Deseja mostrar os dados de qual jogador? (999 para encerrar o programa): '))

    while opcao != 999 and (opcao < 0 or opcao > len(lista_jogadores) - 1):
        opcao = int(input('Opção inválida! Tente novamente ou digite 999 para encerrar o programa: '))

    if opcao <= len(lista_jogadores) - 1:
        print('-=' * 40)
        print(f'* Jogador: {lista_jogadores[opcao]["nome"]}.')
        print(f'* Nº partidas: {lista_jogadores[opcao]["partidas_jogadas"]}.')
        print(f'* Nº gols/partida: ', end='')
        if lista_jogadores[opcao]["partidas_jogadas"] == 0:
            print('Não houve partidas disputadas.')
        else:
            for partida in range(lista_jogadores[opcao]["partidas_jogadas"]):
                print(f'\n  - {partida + 1}ª partida = {lista_jogadores[opcao]["gols_por_partida"][partida]} gol(s)')
        print(f'* Total de gol(s): {lista_jogadores[opcao]["total_gols"]}.')
        print('-=' * 40)

    elif opcao == 999:
        break

print('Programa encerrado!')
# print('-=' * 20)
# print(f'O jogador {estatisticas_jogador["nome"]} jogou {estatisticas_jogador["partidas_jogadas"]} partida(s).')
# for i, v in enumerate(estatisticas_jogador['gols_por_partida']):
#     print(f'Na {i + 1}ª partida fez {v} gol(s)')
# print(f'Foi um total de {estatisticas_jogador["total_gols"]} gol(s)!')
# print('-=' * 20)
