# -*- coding: utf-8 -*-

nome = raw_input("Digite o nome do(a) professor(a):\n")

salarioBruto = float(input("Digite o salário bruto: R$"))
imposto = float(input("Digite o percentual de impostos (Ex.: digite 10 e se percetual for de 10%): "))

percentualImposto = imposto/100

salarioLiquido = salarioBruto - (salarioBruto * percentualImposto)

print("\nNome do(a) professor(a): {0}".format(nome))
print("Salário bruto: R${0}".format(salarioBruto))
print("Imposto: {0}%".format(imposto))
print("Salário Líquido: R${0}".format(salarioLiquido))