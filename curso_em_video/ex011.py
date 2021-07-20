largaParede = float(input('Digite a largura da parede em metros: '))
alturaParede = float(input('Digite a altura da parede em metros: '))
area = alturaParede * largaParede
# sabendo que 1l de tinta pinta 2m²:
tintaNecessaria = area/2
print('Você vai precisar de {}L de tinta para pintar uma área de {}m².'.format(tintaNecessaria, area))
