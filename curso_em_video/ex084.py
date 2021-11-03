nomes_pessoas = []
peso_pessoas = []

lista_pesos_maiores_cem = []
lista_pesos_menores_cem = []

qtd_pessoas = 0

continua = True
while(continua):

    nome = str(input("Digite o nome da pessoa: "))
    nomes_pessoas.append(nome)
    peso = float(input("Digite o peso: "))
    peso_pessoas.append(peso)

    if(peso == max(peso_pessoas)):
        lista_pesos_maiores_cem.append(nome)
    elif(peso == min(peso_pessoas)):
        lista_pesos_menores_cem.append(nome)

    # contabiliza a quantidade de pessoas cadastradas
    qtd_pessoas += 1

    opc = str(input("Deseja continuar cadastrando novas pessoas? [S/N]: ")).strip().upper()[0]

    if('N' in opc):
        break

print('-=' * 30)
print(f'Ao todo foram cadastras {qtd_pessoas} pessoa(s).')
print(lista_pesos_maiores_cem, lista_pesos_menores_cem)
