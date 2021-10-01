from datetime import date
ano_atual = date.today().year

print('\033[1;32m+=\033[m' * 60)
print(f'Estamos em {ano_atual} e queremos saber em qual categoria você se enquadra dentro da Federação Nacional de Natação!')

ano_nascimento = int(input('Informe o ano de seu nascimento: '))
idade = ano_atual - ano_nascimento

if(idade <= 9):
    print('Você faz parte da categoria MIRIM!')
elif(idade > 9 and idade <= 14):
    print('Você faz parte da categoria INFANTIL!')
elif(idade > 14 and idade <= 19):
    print('Você faz parte da categoria JÚNIOR!')
elif(idade > 19 and idade <= 25):
    print('Você faz parte da categoria SÊNIOR!')
else:
    print('Você faz parte da categoria MASTER!')

print('\033[1;32m+=\033[m' * 60)
