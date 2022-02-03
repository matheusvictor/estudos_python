import moeda

preco = float(input('Digite o preço: R$'))
porcentagem_aumento = int(input('Porcentagem de aumento: '))
porcentagem_reducao = int(input('Porcentagem de redução: '))

moeda.resumo(preco, porcentagem_aumento, porcentagem_reducao)
