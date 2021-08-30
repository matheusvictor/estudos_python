def retorna_tempo_arena_em_milisegundos(distancia,velocidade):
  d = float(distancia) * 1000
  tempo = (d / velocidade) * 1000
  return round(tempo)
