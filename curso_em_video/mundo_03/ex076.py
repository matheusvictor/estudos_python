listagem_produtos = ('Lápis', 1.75,
                     'Borracha', 0.70,
                     'Caderno', 20,
                     'Mochila', 150)

for item in listagem_produtos:
    if(type(item) == str):
        # imprimir com alinhamento à esqueda e preencher com pontos até completar 30 caracteres
        print(f'{item:.<30}', end='')
    else:
        print(f'R${item:<.2f}')
