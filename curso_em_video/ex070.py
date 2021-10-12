continua = True
qtd_produtos = produtos_mais_mil = total_gasto = 0
nome_produto_barato = ' '

while(continua):
    preco = float(input('Preço do produto: R$'))
    nome_produto = str(input('Nome do produto: ')).strip()

    menor_preco = preco
    nome_produto_barato = nome_produto

    if (preco > 1000):
        produtos_mais_mil += 1

    if(preco < menor_preco):
        menor_preco = menor_preco
        nome_produto_barato = nome_produto

    total_gasto += preco

    qtd_produtos += 1

    opcao = ' '
    while(opcao not in 'SN'):
        opcao = str(input('Você deseja continuar cadastrando outros produtos?\n[S]-Sim\n[N]-Não\nDigite uma das opções: ')).strip().upper()[0]

    if(opcao == 'N'):
        continua = False

print('=-' * 40)
print(f'Foram cadastrados {qtd_produtos} produto(s) e o gasto total foi de R${total_gasto:.2f}.\n'
      f'Nesta compra houve {produtos_mais_mil} produto(s) que custam mais de R$1000.\n'
      f'O nome do produto mais barato é "{nome_produto_barato}" e custou R${menor_preco:.2f}.')
