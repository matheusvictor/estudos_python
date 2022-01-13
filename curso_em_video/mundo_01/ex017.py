#importando apenas a funcionalidade de calular a hipotenusa da biblioteca math:
from math import hypot
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adj = float(input('Digite o comprimento do cateto adjacente: '))
print(f'O comprimento da hipotenusa é de {hypot(cateto_oposto, cateto_adj):.2f}')