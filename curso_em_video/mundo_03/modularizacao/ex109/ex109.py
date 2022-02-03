import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formata_moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.formata_moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentado {moeda.formata_moeda(preco)} em 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo {moeda.formata_moeda(preco)} em 10%, temos {moeda.diminuir(preco, 10, True)}')
