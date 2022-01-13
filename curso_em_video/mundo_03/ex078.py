valores = list()
maior = menor = 0

for valor in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

qtd_posicoes_maior_numero = qtd_posicoes_menor_numero = 0
posicao_maiores = list()
posicao_menores = list()

for posicao, valor_guardado in enumerate(valores):
    if(valor_guardado == max(valores)):
        qtd_posicoes_maior_numero += 1
        posicao_maiores.append(posicao + 1)
    elif(valor_guardado == min(valores)):
        qtd_posicoes_menor_numero += 1
        posicao_menores.append(posicao + 1)

print(f'Os números digitados foram: {valores}.\n'
      f'Dentre eles, {max(valores)} foi o maior e {min(valores)} foi o menor.')

if(len(posicao_maiores) > 1):
    print(f'Os maiores números aparecem nas posições {posicao_maiores}.')
else:
    print(f'O maior número aparece na posição {posicao_maiores}.')
if(len(posicao_menores) > 1):
    print(f'Os menores números aparecem nas posições {posicao_menores}.')
else:
    print(f'O menor número aparece na posição {posicao_menores}.')
