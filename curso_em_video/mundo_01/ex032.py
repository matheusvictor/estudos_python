from datetime import date # importando biblioteca de datas

ano = int(input("Digite o ano a ser analisado e para saber se ele é bissexto. Caso queira analisar o ano atual, digite 0: "))

if(ano == 0):
    ano = date.today().year # o ano vai ser igual ao ano do dia atual
'''
Chama-se ano bissexto o ano ao qual é acrescentado um dia extra,
ficando com 366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos
(exceto anos múltiplos de 100 que não são múltiplos de 400).
'''

if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO É BISSEXTO!')
