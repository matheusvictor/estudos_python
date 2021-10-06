primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
qntd_termos = int(input('Digite quantos termos dessa P.A você gostaria de exibir: '))

enessimo_termo = primeiro_termo + (qntd_termos - 1) * razao # fórmula para se conhecer o enéssimo termo de uma P.A

print(f'Os {qntd_termos} primeiros termos de uma P.A cujo primeiro termo é {primeiro_termo} e razão é de {razao} são: ',end='')
for contador in range(primeiro_termo, (enessimo_termo + razao), razao):
    print(f'{contador}', end=' ')
