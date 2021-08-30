def calculadistanciabandapercorre(numerorodadaensaios, numeroshows):
    matriz_ensaios = [
        # a   b    c     d    e    f
        [0, 500, 500, 1000, 500, 250],  # a
        [500, 0, 500, 1000, 500, 750],  # b
        [500, 500, 0, 500, 500, 750],  # c
        [1000, 1000, 500, 0, 500, 750],  # d
        [500, 500, 500, 500, 0, 250],  # e
        [250, 750, 750, 750, 250, 0]  # f
    ]

    total_distancia_ensaios = 0

    for integrante in matriz_ensaios:
        for distancia_ensaio in integrante:
            total_distancia_ensaios += distancia_ensaio

    total_distancia_ensaios *= numerorodadaensaios
    total_distancia_ensaios *= 2  # considerando ida e volta.

    matriz_shows = [750, 1250, 1250, 750, 750, 500]  # pub

    total_distancia_show = 0

    for distancia_show in matriz_shows:
        total_distancia_show += distancia_show

    total_distancia_show *= numeroshows
    total_distancia_show *= 2  # considerando ida e volta.

    return (total_distancia_ensaios + total_distancia_show)
