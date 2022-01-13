numero = int(input('Digite quantos termos da sequência de Fibonacci você quer exibir: '))

primeiro_termo = 0
segundo_termo = 1
contador = 3 # pq já conhecemos os dois primeiros termos

print(f'{primeiro_termo} -> {segundo_termo}', end=' -> ')
while(contador <= numero):
    proximo_termo = primeiro_termo + segundo_termo
    print(f'{proximo_termo}', end=' -> ')

    # o primeiro termo passa a ser o segund e o segundo, o próximo
    # para que a soma seja sempre equivalente ao número atual + o anterior
    # ex:
    # primeiro_termo = 1 e segundo_termo = 2
    # proximo_termo = 1 + 2
    # Dps da troca teremos: primeiro_termo = 2 e segundo_termo = 3 (equivalente a soma dos anteriores)
    # Assim, a próxima soma se dará pelo atual primeiro_termo (2, neste caso) + com o atual segundo_termo (3, neste caso).
    # Dessa forma, proximo_termo = 2 + 3 = 5

    primeiro_termo = segundo_termo
    segundo_termo = proximo_termo

    if(contador == numero):
        print('fim')
    contador += 1
