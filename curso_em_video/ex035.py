primeira_reta = int(input("Digite o comprimento da 1ª reta: "))
segunda_reta = int(input("Digite o comprimento da 2ª reta: "))
terceira_reta = int(input("Digite o comprimento da 3ª reta: "))

if(primeira_reta < segunda_reta + terceira_reta and segunda_reta < primeira_reta + terceira_reta and terceira_reta < primeira_reta + segunda_reta):
    print("Os segmentos acima podem formam um triângulo!")
else:
    print("Os segmentos acima não podem formam um triângulo!")
