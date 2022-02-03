import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'Aumentado R${preco} em 10%, temos R${moeda.aumentar(preco, 10)}')
print(f'Diminuindo R${preco} em 10%, temos R${moeda.diminuir(preco, 10)}')
