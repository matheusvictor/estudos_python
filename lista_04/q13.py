def retorna_se_ha_eco_no_estudio(distancia):
  tempo = (distancia / 340)

  print(tempo)
  print(round(tempo,1))

  return round(tempo,1) >= 0.1
