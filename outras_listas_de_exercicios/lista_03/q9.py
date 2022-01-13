nomeProduto = raw_input("Digite o nome do produto:\n")
qtd = int(input("Digite a qtd adquirida:\n"))
precoUnitario = float(input("Digite o valor unitario:\n"))

total = qtd * precoUnitario

if(qtd <= 5):
    desconto = total * 0.02
    totalPagar = total - desconto
elif(qtd > 5 and qtd <= 10):
    desconto = total * 0.03
    totalPagar = total - desconto
else:
    desconto = total * 0.10
    totalPagar = total - desconto

print("\nProduto: {0}\nQtd: {1}\nPreco Unid.: R${2}\nTotal: R${3}\nDesconto: R${4}\nTotal a pagar: R${5}".format(nomeProduto, str(qtd), str(precoUnitario), str(total), str(desconto), str(totalPagar)))