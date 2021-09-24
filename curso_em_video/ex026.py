frase = str(input("Digite uma frase: ")).strip().upper()
qtd_a = frase.count("A")
primeira_vez = frase.find("A") + 1 # lembrando que a primeira ocorrência seria na posição 0. Somamos +1 apenas para ficar mais didático para quem ler a saída
ultima_vez = frase.rfind("A") + 1  # a busca é feita a partir do lado direito da string.
                                   # Logo, a primeira ocorrência da direita para a esquerda é a última ocorrência da esquerda para direita
print(f'Existes {qtd_a} letra(s) "A" nesta frase.\nA primeira corrência da letra "A" é na posição {primeira_vez} e a última é na posição {ultima_vez} (considerando os espaços).')
