from math import tan, cos, sin, radians
angulo = float(input('Digite um valor de ângulo qualquer: '))
angulo_radianos = radians(angulo)
print(f'O ângulo de {angulo}º tem tangente de {tan(angulo_radianos):.2f}, cosseno de {cos(angulo_radianos):.2f} e seno de {sin(angulo_radianos):.2f}.')

