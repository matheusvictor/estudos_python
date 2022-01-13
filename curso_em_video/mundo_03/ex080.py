lista_valores = list()
maior = menor = 0

for contador in range(0, 5):

    valor = int(input('Digite um valor: '))

    # se o contador estiver na primeira posição ou se o número digitado for maior que o último elemento..., o valor
    # digitado ficará na última posição da lista
    if contador == 0 or valor > lista_valores[-1]:
        lista_valores.append(valor)
    # se não, varremos o vetor para...
    else:
        posicao = 0
        while posicao <= len(lista_valores):
            # saber se na posição atual o valor digitado é menor ou igual aos valores inseridos na lista.
            if valor <= lista_valores[posicao]:
                # Caso seja verdade, o valor será adicionado naquela posição da lista
                lista_valores.insert(posicao, valor)
                # quebra o laço e volta para o for e fazer as verificações novamente, até atingir o range definido
                break
            # A variável posicao precisa ser somada +1 para qual o looping voltar:
            posicao += 1

print(f'Os números digitados, em ordem crescente, são: {lista_valores}')



