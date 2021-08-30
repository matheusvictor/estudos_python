def tamanho_setor_busca(areamaior, areamenor):
    secao_area_maior = areamaior / 8
    secao_area_menor = areamenor / 8

    resultado = str(secao_area_maior - secao_area_menor)

    return resultado.rstrip('.0')
