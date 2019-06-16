n1 = float(input("Digite o primeiro numero:\n"))
    
while(True):
    n2 = float(input("Digite o segundo numero:\n"))

    if(n2 == 0):
        print("Valor invalido!")
    else:
        break

divisao = n1 / n2

print("A divisao entre {0} e {1} eh igual a {2}".format(str(n1), str(n2), str(divisao)))