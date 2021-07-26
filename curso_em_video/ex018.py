import math
angulo = float(input('Digite um valor de ângulo qualquer: '))
angulo_radianos = math.radians(angulo)
print(f'O ângulo de {angulo}º tem tangente de {math.tan(angulo_radianos):.2f}, cosseno de {math.cos(angulo_radianos):.2f} e seno de {math.sin(angulo_radianos):.2f}')

