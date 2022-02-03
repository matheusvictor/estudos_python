def fatorial(numero, show=False):
    """
    Calcula o fatorial de um número
    :param numero: número cujo fatorial será calculado
    :param show: Exibe ou não a conta do fatorial (parâmetro opicinal)
    :return: Resultado do fatorial de um número N.
    """
    contador = numero
    fatorial = 1  # inicia variável com fator nulo da multiplicação

    while contador > 0:

        if show:
            print(contador, end='')
            print(' x ' if contador > 1 else ' = ', end='')

        fatorial *= contador  # na 1ª vez do lado, fatorial passará a ser o numero digitado, pois 1 * n = n
        contador -= 1

    return fatorial


print(fatorial(5))
print(fatorial(5, True))
help(fatorial)
