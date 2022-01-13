nome = str(input('Digite seu nome: '))
valor_casa = float(input(f'Olá, {nome}! Digite o valor do imóvel que você deseja comprar: R$'))
salario = float(input('Certo. E qual é o seu salário atual? Digite aqui, por favor: R$'))
tempo_pagamento_anos = int(input(f'Uma última pergunta, {nome}: em quanto tempo (em anos) você vai pagar o financiamento?'
                            f'Digite aqui, por favor: '))

tempo_pagamento_meses = tempo_pagamento_anos * 12
prestacao_mensal = valor_casa / tempo_pagamento_meses
limite_excedente = salario * 0.30

print('=+' * 60)
print(f'Para pagar um imóvel no valor de R${valor_casa:.2f} em {tempo_pagamento_anos} ano(s) a prestação mensal é de'
      f'R${prestacao_mensal:.2f}.')

if(prestacao_mensal > limite_excedente):
    print(f'\033[1;31m{nome}, infelizmente sua solicitação de empréstimo foi negada!\033[m')
else:
    print(f'\033[1;32mParabéns, {nome}! Sua solicitação de empréstimo foi aceita com sucesso!\033[m')
print('=+' * 60)
