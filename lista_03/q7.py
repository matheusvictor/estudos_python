n1 = float(input("Digite um numero:\n"))
n2 = float(input("Digite um numero:\n"))
n3 = float(input("Digite um numero:\n"))


if(n1 > n2 and n1 > n3 and n2 > n3):
    print(n3, n2, n1)
elif(n1 > n2 and n1 > n3 and n2 < n3):
    print(n2, n3, n1)
elif(n2 > n1 and n2 > n3 and n1 > n3):
    print(n3, n1, n2)
elif(n2 > n1 and n2 > n3 and n1 < n3):
    print(n1, n3, n2)
elif(n3 > n1 and n3 > n2 and n1 > n2):
    print(n2, n1, n3)
else:
    print(n1, n2, n3)