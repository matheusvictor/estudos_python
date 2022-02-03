def notas(*pontuacoes, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param pontuacoes: uma ou mais notas dos alunos (aceita-se N notas)
    :param situacao: valor opcional, indicado se deve ou não exibit a situação da turma
    :return: dicionário com informações da turma
    """
    boletim = dict()

    maior_nota = menor_nota = pontuacoes[0]
    for nota in pontuacoes:
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota

    boletim['total'] = len(pontuacoes)
    boletim['maior_nota'] = maior_nota
    boletim['menor_nota'] = menor_nota
    boletim['média'] = sum(pontuacoes) / len(pontuacoes)

    if situacao:
        if boletim['média'] >= 7.0:
            boletim['situação'] = 'BOA'
        elif 7.0 > boletim['média'] >= 5.0:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'RUIM'

    return boletim


print(notas(5.5, 9.5, 10, 6.5))
print(notas(9, 10, 5.5, 2.5, 8.5, situacao=True))
print(notas(3.5, 10, 6.5, situacao=True))
print(notas(3.5, 2, 6.5, situacao=True))
