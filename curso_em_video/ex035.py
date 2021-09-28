primeira_reta = int(input("Digite o comprimento da 1ª reta: "))
segunda_reta = int(input("Digite o comprimento da 2ª reta: "))
terceira_reta = int(input("Digite o comprimento da 3ª reta: "))

if(primeira_reta < segunda_reta + terceira_reta and segunda_reta < primeira_reta + terceira_reta and terceira_reta < primeira_reta + segunda_reta):
    print("\033[1;30;42mOs segmentos acima podem formam um triângulo!\033[m")
else:
    print("\033[1;7;30;41mOs segmentos acima não podem formam um triângulo!\033[m")
