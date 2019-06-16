for linha in range(1, 12):
    seq = ''
    for coluna in range(1, linha):
        seq += "{0} ".format(str(coluna))
    print(seq)