ano = int(input("Digit o ano para saber se ele é bissexto: "))

'''
Chama-se ano bissexto o ano ao qual é acrescentado um dia extra,
ficando com 366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos
(exceto anos múltiplos de 100 que não são múltiplos de 400).
'''

if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} é não é NÃO É BISSEXTO!')
