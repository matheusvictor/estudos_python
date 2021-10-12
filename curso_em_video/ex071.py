#inicializando contador de notas
qtd_notas = 0

saque = int(input('Valor a ser sacado: R$'))
valor_atual = saque
maior_nota = 50

while(True):
    if(valor_atual >= maior_nota):
        valor_atual -= maior_nota
        qtd_notas += 1
    #se valor_atual for menor que maior_nota...
    else:
        if(qtd_notas > 0):
            print(f'{qtd_notas} cédula(s) de R${maior_nota}.')
        #verifico se a maior_nota ainda é a de R$50
        if(maior_nota == 50):
            #se a maior_nota for a de R$50, ela passa a ser a de R$20, já que meu valor_atual é menor que R$50
            maior_nota = 20
        elif(maior_nota == 20):
            maior_nota = 10
        elif(maior_nota == 10):
            maior_nota = 1
        qtd_notas = 0 #zerando o contado para o próximo loop
        if(valor_atual == 0):
            break
