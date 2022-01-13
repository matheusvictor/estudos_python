acumulador = 0
qtdPessoas = 10
i = 0

for i in range(i, qtdPessoas):
    idade = int(input("Digite a idade da pessoa numero {0}:\n".format(str(i+1))))
    acumulador += idade

mediaIdade = acumulador / qtdPessoas
print("\nA idade media entre as idades eh igual a {0}".format(str(mediaIdade)))