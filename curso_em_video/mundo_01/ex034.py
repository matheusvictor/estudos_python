salario = float(input("Digite o valor do salário: R$"))

if(salario > 1250):
    aumento = 0.10
else:
    aumento = 0.15

novo_salario = salario + (salario * aumento)

print(f'O salário de {salario:2f} com aumento de {int(aumento * 100)}% é igual a R${novo_salario:.2f}')
