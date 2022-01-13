nome = str(input("Digite seu nome: ")).strip() # explicitando que a entrada deve ser uma string e eliminando espaços inseridos antes ou depois do nome digitado
nome_dividido = nome.split()
nome_em_maiusculo = nome.upper()
nome_em_minusculo = nome.lower()
qtd_espacos = nome.count(" ")
tamanho_nome_sem_espacos = len(nome) - qtd_espacos

print(f'Nome em maiúsculo: {nome_em_maiusculo}.')
print(f'Nome em minúsculo: {nome_em_minusculo}.')
print(f'Qtd. de letras no nome completo (sem considerar espaços): {tamanho_nome_sem_espacos}.')
print(f'Qtd. de letras no primeiro nome: {len(nome_dividido[0])}.')
