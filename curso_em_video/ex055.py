lista_pesos = []

for contador in range(0,5):
    peso = float(input(f'Digite o peso (em Kg) da {contador+1}ª pessoa: '))
    lista_pesos.append(peso)

print(f'O maior peso lido foi {max(lista_pesos)}kg e o menor foi {min(lista_pesos)}kg.')
