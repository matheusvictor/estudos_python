from datetime import date
ano_atual = date.today().year
maior_idade = 0
menor_idade = 0

for contador in range(0,7):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {contador + 1}ª pessoa: '))

    if(ano_atual - ano_nascimento >= 21): #considerando 21 anos como maior idade.
        maior_idade += 1
    else:
        menor_idade += 1

print(f'Maior(es) de idade: {maior_idade}.\nMenor(es) de idade: {menor_idade}.')
