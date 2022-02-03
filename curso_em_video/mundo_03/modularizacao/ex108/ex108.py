import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formata_moeda(preco)} é {moeda.formata_moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.formata_moeda(preco)} é {moeda.formata_moeda(moeda.dobro(preco))}')
print(f'Aumentado {moeda.formata_moeda(preco)} em 10%, temos {moeda.formata_moeda(moeda.aumentar(preco, 10))}')
print(f'Diminuindo {moeda.formata_moeda(preco)} em 10%, temos {moeda.formata_moeda(moeda.diminuir(preco, 10))}')
