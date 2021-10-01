preco = float(input("Digite o preço do produto: R$"))
print('\033[1;31m+=\033[m' * 40)
print(f'Formas de pagamento:')
print('''1-À vista no dinheiro/cheque
2-À vista no cartão
3-Cartão de crédito (até 2x)
4-Cartão de crédito (3x ou mais)''')
opcao = int(input('Digite a opção desejada: '))

preco_final = preco

print('\033[1;31m+=\033[m' * 40)
if(opcao == 1):
    preco_final = preco - (preco * 0.10)
    print('Você optou por pagar à vista (dinheiro/cheque) e terá um desconto de 10%.')
elif(opcao == 2):
    preco_final = preco - (preco * 0.05)
    print('Você optou por pagar à vista no cartão e terá um desconto de 5%.')
elif(opcao == 3):
    valor_parcelas = preco / 2
    print(f'Você optou pagar em 2 parcelas de R${valor_parcelas:.2f}.')
else:
    quantidade_parcelas = int(input('Você quer dividir em quantas parcelas? Digite aqui: '))
    if(quantidade_parcelas < 3):
        print('Erro! Programa encerrado!')
        exit()
    else:
        preco_final = preco + (preco * 0.20)
        valor_parcelas = preco_final / quantidade_parcelas
        print(f'Você optou por pagar em {quantidade_parcelas} de parcelas.\nEssa forma de pagamento tem ainda 20% de juros no valor final do produto.\nPortanto, o valor de cada parcela é de R${valor_parcelas:.2f}.')

print(f'O valor original do produto é de R${preco:.2f}')
print(f'O valor final do produto é de R${preco_final:.2f}.')
print('\033[1;31m+=\033[m' * 40)
