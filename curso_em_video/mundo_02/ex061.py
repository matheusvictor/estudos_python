primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
qntd_termos = int(input('Digite quantos termos dessa P.A você gostaria de exibir: '))
contador = 1
print(f'Os {qntd_termos} primeiros termos de uma P.A cujo primeiro termo é {primeiro_termo} e razão é de {razao} são: ',end='')
while(contador <= qntd_termos):
    print(primeiro_termo, end=' ')
    primeiro_termo += razao
    contador += 1
