i = 0
x = float(input("Digite um numero:\n"))

if(x <= 1):
    print("Nao ha numeros inteiros entre {0} e {1}".format(str(i), str(x)))
else:
    xInt = int(x) #considera apenas a parte inteira, mesmo que o numeor digitado anteriormente tenha casas decimais
    print("O(s) numero(s) inteiro(s) entre " + str(i) + " e " + str(xInt) + " eh(sao):")
    for cont in range (1, xInt):
        print(str(cont))