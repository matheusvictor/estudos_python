"""
Style                      Text          Background
=========================================================
0 (sem estilo)              30              40      (branco)
1 (negrito)                 31              41      (vermelho)
4 (sublinhado)              32              42      (verde)
7 (inverter cores)          33              43      (amarelo)
                            34              44      (azul)
                            35              45      (roxo)
                            36              46      (ciano)
                            37              47      (cinza)
"""

print('\033[31mOlá, mundo!')
print('\033[1;7;30;43mEstou colocando cores no Python!\033[m')
