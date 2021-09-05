from random import shuffle
aluno_um = input('Digite o nome do primeiro aluno: ')
aluno_dois = input('Digite o nome do segundo aluno: ')
aluno_tres = input('Digite o nome do terceiro aluno: ')
aluno_quatro = input('Digite o nome do quarto aluno: ')
lista_alunos = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]
shuffle(lista_alunos)
print(f'A ordem das apresentações será: {lista_alunos}.')
