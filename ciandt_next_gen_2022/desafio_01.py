import math

def retorna_tempo_minimo_em_minutos(p, s, n):
    tempo_minutos = s / 60
    pessoas_portas = math.ceil(p / n)
    return math.ceil(pessoas_portas * tempo_minutos)
