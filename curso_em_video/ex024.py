nome_cidade = str(input("Digite o nome de uma cidade: ")).strip()
nome_cidade_dividido = nome_cidade.split()
primeiro_nome_cidade = nome_cidade_dividido[0].upper()

print("SANTO" in primeiro_nome_cidade)
