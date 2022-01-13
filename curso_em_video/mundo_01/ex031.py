distancia_viagem = float(input("Digite a distância a ser percorrida na viagem: "))
preco_viagem = 0

if(distancia_viagem <= 200):
    preco_viagem = distancia_viagem * 0.50
else:
    preco_viagem = distancia_viagem * 0.45

print(f'Numa viagem de {distancia_viagem}km, você pagará R${preco_viagem:.2f}.')
