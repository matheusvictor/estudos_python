n1 = float(input("Digite primeiro numero:\n"))
soma = 0

while(True):
    n2 = float(input("Digite o segundo numero:\n"))
    if(n2 == n1):
        print("\O segundo numero nao pode ser igual ao primeiro.\n")
    else:
        break
while(True):
    n3 = float(input("Digite o terceiro numero:\n"))
    if(n3 == n2):
        print("\O terceiro numero nao pode ser igual ao segundo.\n")
    elif(n3 == n1):
        print("\O terceiro numero nao pode ser igual ao primeiro.\n")
    else:
        break
if(n1 > n2 and n1 > n3 and n2 > n3):
    soma = n1 + n2
elif(n1 > n2 and n1 > n3 and n2 < n3):
    soma = n1 + n3
elif(n2 > n1 and n2 > n3 and n1 < n3):
    soma = n2 + n3
elif(n2 > n1 and n2 > n3 and n1 > n3):
    soma = n2 + n1
elif(n3 > n1 and n3 > n2 and n1 > n2):
    soma = n3 + n1
else:
    soma = n3 + n2

print("A soma entre os maiores numeros digitados eh igual a {0}".format(str(soma)))