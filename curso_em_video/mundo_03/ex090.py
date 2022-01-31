nome = str(input('Nome: '))
media = float(input(f'Digite a média de {nome}: '))

if media >= 7.0:
    situacao = 'APROVADO(A)'
else:
    situacao = 'REPROVADO(A)'

dicionario = {'nome': nome, 'media': media, 'situacao': situacao}

print('-=' * 15)
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')
print('-=' * 15)
