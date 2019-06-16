n1 = 0
n2 = 0

for i in range(2):
    numero = float(input("Digite um numero:\n"))

    while(numero == 0 and i == 1):
        numero = float(input("Valor invalido! Digite novamente o segundo numero:\n"))

    if(numero != 0 and i == 0):
        n1 = numero
    if(numero != 0 and i == 1):
        n2 = numero

divisao = n1/n2

print("A divisao entre {0} e {1} eh igual a {2}".format(str(n1), str(n2), str(divisao)))