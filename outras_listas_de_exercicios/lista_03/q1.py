n = float(input("Digite um numero:\n"))

if(n > -1 and n < 1):
    print(str(n) + " fica entre 1 e -1.")
elif(n > 20 and n < 30):
    print(str(n) + " fica entre 20 e 30.")
else:
    print(str(n) + " nao pertence aos intervalos entre 20 e 30, ou de 1 e -1.")