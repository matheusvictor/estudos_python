# Boletim com listas compostas: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
# composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de
# cada aluno individualmente.

turma = list()
aluno = []

while True:
    nome_aluno = str(input('Nome do(a) aluno(a): '))
    primeira_nota = float(input(f'1ª nota de {nome_aluno}: '))
    segunda_nota = float(input(f'2ª nota de {nome_aluno}: '))

    aluno.append(nome_aluno)
    aluno.append(primeira_nota)
    aluno.append(segunda_nota)
    aluno.append((primeira_nota + segunda_nota) / 2)

    turma.append(aluno[:])
    aluno.clear()

    resposta = str(input('Deseja continuar? [S/N]: '))
    if resposta in 'Nn':
        break

print('-=' * 20)
print(f'{"Nº":<20}{"NOME":<10}{"MÉDIA":>10}')
print('-=' * 20)

for indice, aluno in enumerate(turma):
    print(f'{indice:<20}{aluno[0]:<10}{aluno[-1]:>10.1f}')

print('-=' * 20)

while True:

    opc = int(input('Mostrar nota de qual aluno(a)? (999 para sair): '))

    if opc == 999:
        print('VOLTE SEMPRE!')
        break
    elif opc <= len(turma) - 1:
        print(f'As notas de {turma[opc][0]} foram {turma[opc][1]} e {turma[opc][2]}.')
