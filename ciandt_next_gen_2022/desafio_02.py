import math

def retorna_pessoas_preferem_um_unico_palco(quantidade_pessoas_evento):
    palco_a = (quantidade_pessoas_evento * 0.45)
    palco_b = (quantidade_pessoas_evento * 0.33)
    palco_c = (quantidade_pessoas_evento * 0.34)

    palco_ab = (quantidade_pessoas_evento * 0.20)
    palco_ac = (quantidade_pessoas_evento * 0.18)
    palco_bc = (quantidade_pessoas_evento * 0.10)
    palco_abc = (quantidade_pessoas_evento * 0.03)

    somente_palco_a = palco_a - ((palco_ab - palco_abc) + (palco_ac - palco_abc) + palco_abc)
    somente_palco_b = palco_b - ((palco_ab - palco_abc) + (palco_bc - palco_abc) + palco_abc)
    somente_palco_c = palco_c - ((palco_ac - palco_abc) + (palco_bc - palco_abc) + palco_abc)

    return math.floor(somente_palco_a + somente_palco_b + somente_palco_c)
