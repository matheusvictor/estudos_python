velocidade_autorizada = 80.0
velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80.0:
    multa = (velocidade - velocidade_autorizada) * 7
    print(f'Você foi multado em R${multa:.2f} por excesso de velocidade!')
else:
    print(f'Você está a {velocidade}km/h. Portanto, dentro da velocidade permitida. Dirija com segurança.')
