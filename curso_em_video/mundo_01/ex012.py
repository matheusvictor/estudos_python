preco = float(input('Digite o preço do produto: R$'))
precoDesconto = preco - (preco * 0.05)
print('Preço com desconto de 5%: R${:.2f}.'.format(precoDesconto))
