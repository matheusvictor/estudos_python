expressao = str(input('Digite a expressão que deseja analisar: ')).strip()

numero_parentese_abertos = expressao.count('(')
numero_parentese_fechados = expressao.count(')')
total_parenteses = numero_parentese_abertos + numero_parentese_fechados

if(total_parenteses % 2 == 0):
    print('Expressão VÁLIDA!')
else:
    print('Expressão INVÁLIDA!')


