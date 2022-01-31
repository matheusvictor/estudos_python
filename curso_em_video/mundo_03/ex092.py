from datetime import date

ano_atual = date.today().year
tempo_contribuicao = 35

nome = str(input('Nome: '))
ano_nascimento = int(input('Ano nascimento: '))
idade = ano_atual - ano_nascimento
carteira = int(input('Carteira de trabalho (digite 0 se não tiver): '))

dados = {'nome': nome, 'idade': idade, 'ctps': carteira}

if carteira != 0:
    dados['ano_contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano_contratação'] + tempo_contribuicao) - ano_atual)

print('-=' * 30)
for chave, valor in dados.items():
    print(f'{chave}: {valor}')
