n = float(input("Digite um numero:\n"))

if(not(n > 15 and n < 100)):
    print(str(n) + " nao esta no intervalo entre 15 e 100.")
else:
    print(str(n) + " esta no intervalo entre 15 e 100.")