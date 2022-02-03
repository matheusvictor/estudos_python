from curso_em_video.mundo_03.modularizacao.ex111.utilidadescev import moeda

preco = float(input('Digite o preço: R$'))
porcentagem_aumento = int(input('Porcentagem de aumento: '))
porcentagem_reducao = int(input('Porcentagem de redução: '))

moeda.resumo(preco, porcentagem_aumento, porcentagem_reducao)
