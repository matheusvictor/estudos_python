limite = int(input("Digite a qtd de numeros que deseja inserir:\n"))
i = 0
qtdPares = 0

for i in range(limite):
    numero = float(input("Digite um numero:\n"))
    
    if(numero % 2 == 0):
        print("{0} eh par.\n".format(str(numero)))
        qtdPares += 1
    else:
        print("{0} eh impar.\n".format(str(numero)))

print("Voce digitou {0} numero(s) par(es)".format(str(qtdPares)))