numero = input("Digite um número qualquer: ")
numero = numero.rjust(4,'0')

milhar = int(numero[0])
centena = int(numero[1])
dezena = int(numero[2])
unidade = int(numero[3])

print(f'milhar: {milhar}')
print(f'centena: {centena}')
print(f'dezena: {dezena}')
print(f'unidade: {unidade}')
