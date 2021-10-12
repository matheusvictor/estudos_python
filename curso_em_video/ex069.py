continua = True
qtd_pessoas = maiores_dezoito = mulheres_menores_vinte = qtd_homens = 0

while(continua):
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' ' #inicializa variável vazia

    while(sexo not in 'MF'):
        sexo = str(input('Digite o sexo da pessoa [F/M]: ')).strip().upper()[0] #considerando somente a primeira letra digitada

    if(idade > 18):
        maiores_dezoito += 1
    if('M' in sexo):
        qtd_homens += 1
    if('F' in sexo and idade < 20):
        mulheres_menores_vinte += 1

    qtd_pessoas += 1

    opcao = ' '
    while(opcao not in 'SN'):
        opcao = str(input('Você deseja continuar cadastrando outras pessoas?\n[S]-Sim\n[N]-Não\nDigite uma das opções: ')).strip().upper()[0]

    if(opcao == 'N'):
        continua = False

print(f'Foram cadastradas {qtd_pessoas} pessoa(s). Sendo que {maiores_dezoito} delas são maiores de 18 anos.\n'
      f'Neste grupo há {mulheres_menores_vinte} mulher(es) menor(es) de vinte anos. Qtd. de homen: {qtd_homens}.')
