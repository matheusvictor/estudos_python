from datetime import date
ano_atual = date.today().year

print('\033[1;31m+=\033[m' * 50)
print(f'Estamos em {ano_atual} e queremos saber se você já tem idade para se apresentar ao Serviço Militar.')
opcao = int(input('Para começar: você é do sexo masculino?\n1-Sim\n2-Não\nDigite uma das opções acima: '))

if(opcao == 2):
    print('\nVocê não precisa se alistar!')
    exit() #finaliza o programa

ano_nascimento = int(input('Informe o ano de seu nascimento: '))
idade = ano_atual - ano_nascimento

print('\033[1;31m+=\033[m' * 50)

if(idade > 18):
    print(f'Você tem {idade} anos. Já passou da hora de se alistar!\nO alistamento é obrigatório aos 18 anos de idade para cidadãos brasileiros do sexo masculino.'
          f'\nSeu alistamento deveria ter sido feito em {ano_nascimento+18}. Você passou {idade-18} ano(s) do prazo!')
elif(idade == 18):
    print(f'Você tem {idade} anos. Está na hora se alistar!\nO alistamento é obrigatório aos 18 anos de idade para cidadãos brasileiros do sexo masculino.')
else:
    print(f'Você tem {idade} anos.\nO alistamento é obrigatório aos 18 anos de idade para cidadãos brasileiros do sexo masculino.\nFaltam {18-idade} ano(s) para você se apresentar.')

print('\033[1;31m+=\033[m' * 50)
