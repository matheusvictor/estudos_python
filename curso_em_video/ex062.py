primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
qntd_termos = int(input('Digite quantos termos dessa P.A você gostaria de exibir: '))

termos_a_mostrar = 0
contador = 0

while(qntd_termos != 0):
    termos_a_mostrar += qntd_termos # na primeira vez, esse valor será igual ao número de termos inseridos pelo usuário

    while(contador < termos_a_mostrar):
        print(f'{primeiro_termo}', end=' ')
        primeiro_termo += razao
        contador += 1

    qntd_termos = int(input('\nVocê quer mostrar quantos termos a mais? Digite aqui: '))
print(f'Progressão finalizada com {termos_a_mostrar} termo(s) exibido(s).')
