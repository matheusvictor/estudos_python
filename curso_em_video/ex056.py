# inicializando variáveis de controle
somas_idades = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
qtd_mulheres = 0
mulheres_menos_vinte_anos = 0

# iniciando o programa
qnt_pessoas = int(input('Digite a quantidade de pessoas que compõe o grupo: '))
if(qnt_pessoas == 1):
    print('\033[31mPrograma encerrado!\033[m')
    print('É preciso que haja pelo menos duas pessoas para compor o grupo. Reinicie o programa e tente novamente.')
    exit()
else:
    for contador in range(1, qnt_pessoas+1): # irá se repetir n vezes, a depender do valor digitado acima
        print('-=' * 10, f'{contador}ª PESSOA', '-=' * 10)
        nome = str(input(f'Nome: ')).strip()
        idade = int(input(f'Idade: '))
        sexo = str(input(f'Sexo: ')).strip().upper()

        somas_idades += idade # acumula a soma total das idades inseridas

        if('M' in sexo and idade > idade_homem_mais_velho): # verifica se há a letra M (maíuscula ou minúscula) na variável sexo
            nome_homem_mais_velho = nome
            idade_homem_mais_velho = idade

        if('F' in sexo):
            # contabiliza a quantidade de mulheres presentes no grupo
            qtd_mulheres += 1
            if(idade < 20):
                mulheres_menos_vinte_anos += 1

# exibindo resultados...
print(f'\nA soma das idades dessas {qnt_pessoas} pessoas é igual a {somas_idades}.'
      f'A média de idade do grupo é igual a {somas_idades/qnt_pessoas}.')
print(f'O homem mais velho se chama {nome_homem_mais_velho} e ele tem {idade_homem_mais_velho} anos.')
print(f'No grupo há {qtd_mulheres} mulheres e {mulheres_menos_vinte_anos} delas têm menos de 20 anos.')
