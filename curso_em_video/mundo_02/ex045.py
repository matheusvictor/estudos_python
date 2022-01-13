from random import randint
from time import sleep # adiciona módulo sleep
print('Vamos jogar '
      '\033[1;31mJO\033[m'
      '\033[1;32mKEN\033[m'
      '\033[1;33mPÔ\033[m?!')
opcao = int(input('1-Sim\n2-Não\nDigite uma opção: '))
print('+=' * 40)
if(opcao == 2 or opcao != 1):
      print('Programa encerrado!')
      print('+=' * 40)
      exit()
else:
      escolhas_possiveis = ('\033[1;31mPEDRA\033[m', '\033[1;32mPAPEL\033[m', '\033[1;33mTESOURA\033[m')
      escolha_computador = randint(0,2) # considerando que a lista acima começa do índica 0

      print('OBA! Será que você consegue me vencer?! Essas são as opções:')
      print('[0] - Pedra\n[1] - Papel\n[2] - Tesoura')
      escolha_usuario = int(input('Qual é sua escolha? Digite uma das opções acima: '))
      print('+=' * 40)

      if(escolha_usuario < 0 or escolha_usuario > 2):
            print('Opção inválida! Programa encerrado!')
            exit()

      print('\033[1;31mJO\033[m')
      sleep(1) # aguarda 1 segundo antes de imprimir a próxima linha
      print('\033[1;32mKEN\033[m')
      sleep(1)
      print('\033[1;33mPÔ\033[m!!!')
      print(f'Você escolheu {escolhas_possiveis[escolha_usuario]} e eu, {escolhas_possiveis[escolha_computador]}.')

      if(escolha_usuario == escolha_computador):
            print(f'Hum... Você é mesmo bom, hein! Eu também escolhi {escolhas_possiveis[escolha_computador]}. Tivemos um empate!')
      else:
            if(escolha_usuario == 0 and escolha_computador == 1):
                  print('HAHA!, você perdeu!')
            elif(escolha_usuario == 0 and escolha_computador == 2):
                  print('Droga, você ganhou!')
            elif(escolha_usuario == 1 and escolha_computador == 2):
                  print('HAHA!, você perdeu!')
            elif(escolha_usuario == 1 and escolha_computador == 0):
                  print('Droga, você ganhou!')
            elif(escolha_usuario == 2 and escolha_computador == 0):
                  print('HAHA!, você perdeu!')
            else:
                  print('Droga, você ganhou!')

print('+=' * 40)
