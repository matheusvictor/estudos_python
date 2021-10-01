nome = str(input('Digite seu nome: '))
valor_casa = float(input(f'Olá, {nome}! Digite o valor do imóvel que você deseja comprar: R$'))
salario = float(input('Certo. E qual é o seu salário atual? Digite aqui, por favor: R$'))
tempo_pagamento = int(input(f'Uma última pergunta, {nome}: em quanto tempo (em meses) você vai pagar o empréstimo? Digite aqui, por favor: '))

prestacao_mensal = valor_casa / tempo_pagamento
limite_excedente = salario * 0.30

if(prestacao_mensal > limite_excedente):
    print(f'\033[1;31m{nome}, infelizmente sua solicitação de empréstimo foi negada!\033[m')
else:
    print(f'\033[1;32mParabéns, {nome}! Sua solicitação de empréstimo foi aceita com sucesso!\033[m')
