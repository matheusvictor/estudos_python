from random import randint
print('Vamos jogar '
      '\033[1;31mJO\033[m'
      '\033[1;32mKEN\033[m'
      '\033[1;33mPÔ\033[m?!')
opcao = int(input('1-Sim\n2-Não\nDigite uma opção: '))
print('+=' * 40)
if(opcao == 2):
      print('Programa encerrado!')
      print('+=' * 40)
      exit()
else:
      escolha_computador = randint(1,3)

      if(escolha_computador == 1):
            escolha_computador_texto = 'Pedra'
      elif(escolha_computador == 2):
            escolha_computador_texto = 'Papel'
      else:
            escolha_computador_texto = 'Tesoura'

      print('OBA! Será que você consegue me vencer?! Essas são as opções:')
      print('1-Pedra\n2-Papel\n3-Tesoura')
      escolha_usuario = int(input('Qual é sua escolha? Digite uma das opções acima: '))

      if(escolha_usuario == 1 and escolha_computador == 3):
            print('Droga, você ganhou! Você escolheu pedra e eu, tesoura.')
      elif(escolha_usuario == 1 and escolha_computador == 2):
            print('HAHA!, você perdeu! Você escolheu pedra e eu, papel.')
      elif(escolha_usuario == 2 and escolha_computador == 1):
            print('Droga, você ganhou! Você escolheu papel e eu, pedra.')
      elif(escolha_usuario == 2 and escolha_computador == 3):
            print('HAHA!, você perdeu! Você escolheu papel e eu, tesoura.')
      elif(escolha_usuario == 3 and escolha_computador == 2):
            print('Droga, você ganhou! Você escolheu tesoura e eu, papel.')
      elif(escolha_usuario == 3 and escolha_computador == 1):
            print('HAHA!, você perdeu! Você escolheu tesoura e eu, pedra.')
      else:
            print(f'Hum... Você é mesmo bom, hein! Eu também escolhi {escolha_computador_texto}. Tivemos um empate!')
print('+=' * 40)
