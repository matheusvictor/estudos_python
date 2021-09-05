# importa o método choice do módulo random:
from random import choice
aluno_um = input('Digite o nome do primeiro aluno: ')
aluno_dois = input('Digite o nome do segundo aluno: ')
aluno_tres = input('Digite o nome do terceiro aluno: ')
aluno_quatro = input('Digite o nome do quarto aluno: ')
lista_alunos = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]
aluno_escolhido = choice(lista_alunos)
print(f'{aluno_escolhido} foi escolhido(a) para apagar o quadro da sala!')
