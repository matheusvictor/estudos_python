pessoa = dict()
lista_pessoas = list()
lista_mulheres = list()
soma_idades = media_idade = 0

continua = True
while continua:
    pessoa['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo [M/F]: '))

    while sexo not in 'MmFf':
        sexo = str(input('ERRO! Digite apenas M ou F: '))
    pessoa['sexo'] = sexo.upper()[0]

    if pessoa['sexo'] in 'Ff':
        lista_mulheres.append(pessoa.copy())

    pessoa['idade'] = int(input(f'Idade de {pessoa["nome"]}: '))
    soma_idades += pessoa['idade']

    lista_pessoas.append(pessoa.copy())
    media_idade = soma_idades / len(lista_pessoas)
    pessoa.clear()

    opc = str(input('Deseja continuar? [S/N]: '))

    while opc not in 'SsNn':
        opc = str(input('Opção inválida! Tente novamente [S/N]: ')).upper()[0]

    if opc in 'Nn':
        continua = False
        break

print('-=' * 20)
print(f'* Ao todo foram cadastradas {len(lista_pessoas)}.')
print(f'* A média de idade é de {soma_idades / len(lista_pessoas):5.2f} anos')
print(f'* As pessoas de sexo Feminino foram: ')
for pessoa in lista_pessoas:
    if pessoa['sexo'] in 'Ff':
        print(f'  - {pessoa["nome"]}')
print(f'* As pessoas com idade acima da média foram: ')
for pessoa in lista_pessoas:
    if pessoa['idade'] >= media_idade:
        print(f'  - {pessoa["nome"]}')
