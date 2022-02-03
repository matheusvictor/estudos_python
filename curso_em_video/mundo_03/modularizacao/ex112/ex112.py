from curso_em_video.mundo_03.modularizacao.ex112.utilidadescev import moeda, dado

preco = dado.leiaDinheiro('Digite o preço: R$')
porcentagem_aumento = int(input('Porcentagem de aumento: '))
porcentagem_reducao = int(input('Porcentagem de redução: '))

moeda.resumo(preco, porcentagem_aumento, porcentagem_reducao)
