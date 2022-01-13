nome_completo = str(input("Digite um nome: ")).strip()
nome_dividido = nome_completo.split()
print(f'Primeiro nome: {nome_dividido[0]}\nÚltimo nome: {nome_dividido[-1]}')
