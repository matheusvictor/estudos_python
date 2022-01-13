from random import sample, randint

# a. método não tão escalonável:
# tupla_numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

# b. método utilizando sample():
# tupla_numeros = tuple(sample(range(10), 5))

# O sample() é um método usado para retornar uma lista
# com uma seleção aleatória de um número específico de itens dentro de uma sequência.
# Esse caso, vai retornar uma lista de 5 itens dentro de um range de 10 números

# c. método com for dentro da tupla:
tupla_numeros = tuple(randint(1, 10) for i in range(10))

print(f'Foram gerados os seguintes números: {tupla_numeros}.')
print(f'Dentre eles, o maior valor é {max(tupla_numeros)} e o menor é {min(tupla_numeros)}.')
