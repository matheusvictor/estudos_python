km_rodados = float(input('Quantos km você percorreu com o carro alugado?: '))
dias_alugados = int(input('Você alugou o carro por quantos dias?: '))
valor_aluguel = (60 * dias_alugados) + (0.15 * km_rodados)
print(f'O total a pagar pelo aluguel é R${valor_aluguel:.2f}')
