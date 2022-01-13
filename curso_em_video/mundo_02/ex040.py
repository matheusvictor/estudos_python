primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))

media = (primeira_nota + segunda_nota) / 2

if(media >= 7):
    print('Aprovado(a)!')
elif(media >= 5 and media <= 6.9):
    print('Recuperação!')
else:
    print('Reprovado(a)!')
    