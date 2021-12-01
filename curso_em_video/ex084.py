lista_temporaria = []
lista_pessoas = []
maior_peso = menor_peso = 0  # inicializando variáveis de controle para peso

continua = True
while (continua):

    nome = str(input("Digite o nome da pessoa: "))
    lista_temporaria.append(nome)
    peso = float(input("Digite o peso: "))
    lista_temporaria.append(peso)

    if (len(lista_pessoas) == 0):  # se a lista_pessoas estiver vazia...
        # o maior_peso é igual ao menor_peso que é igual ao peso inserido em lista_temporaria
        # referenciamos o índice [1] para pegar o valor númerico, pois estamos utilizando o índice [0] para guardar o nome (str)
        maior_peso = menor_peso = lista_temporaria[1]
    else:
        # se não, verificamos se, no próximo retorno aaao laço, o novo valor inserido em lista_temporaria[1]
        # é maior que aquele guardado na variável maior_peso
        if (lista_temporaria[1] > maior_peso):
            # caso verdadeiro, maior_peso assumirá esse novo valor
            maior_peso = lista_temporaria[1]
        if (lista_temporaria[1] < menor_peso):
            menor_peso = lista_temporaria[1]

    lista_pessoas.append(lista_temporaria[:])  # adiciona uma cópia dos dados de lista_temporaria na lista_pessoas
    lista_temporaria.clear()  # zera a lista_temporaria para receber novos valores e manter as ref. sempre nos índices 0 e 1

    opc = str(input("Deseja continuar cadastrando novas pessoas? [S/N]: ")).strip().upper()[0]

    if ('N' in opc):
        break

print('-=' * 30)
print(f'Ao todo foram cadastras {len(lista_pessoas)} pessoa(s). Sendo elas: {lista_pessoas}')
print(f'O maior peso foi de {maior_peso}kg. Pessoas que se enquadram neste grupo: ', end='')
# para cada pessoa armazenada em lista_pessoas
for pessoa in lista_pessoas:
    # verificamos se o peso dela é igual a maior_peso
    # usamos o índice 1 em lista_pessoas, pois é aí que estamos guardando os pesos.
    if pessoa[1] == maior_peso:
        # imprimimos o nome da pessoa, que está armazenado no índice 0 da lista
        print(f'{pessoa[0]}', end='')
print(f'O maior peso foi de {menor_peso}kg. Pessoas que se enquadram neste grupo: ', end='')
for pessoa in lista_pessoas:
    if pessoa[1] == menor_peso:
        print(f'{pessoa[0]}', end='')
