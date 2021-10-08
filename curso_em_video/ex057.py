sexo = str(input('Digite o sexo da pessoa [F/M]: ')).strip().upper()

while('M' not in sexo and 'F' not in sexo):
    sexo = str(input('Entrada inválida. Tente novamente: ')).strip().upper()