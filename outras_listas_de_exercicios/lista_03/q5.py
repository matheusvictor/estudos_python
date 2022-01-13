n1 = int(input("Digite o primeiro numero:\n"))
n2 = int(input("Digite o segundo numero:\n"))

if(n1 > n2):
    print("\nOs valores entre {0} e {1} sao:\n".format(str(n1), str(n2)))
    for n2 in range(n2+1, n1):
        print(n2)
elif(n2 > n1):
    print("\nOs valores entre {0} e {1} sao:\n".format(str(n2), str(n1)))
    for n2 in range(n2-1, n1, -1):
        print(n2)
else:
    print("\nOs valores sao iguais")