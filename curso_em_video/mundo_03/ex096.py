def calcula_area(largura, comprimento):
    print(f'A área do seu terreno de {largura}x{comprimento} é de {largura * comprimento}m².')


largura = float(input('Digite a largura do terreno, em metros: '))
comprimento = float(input('Digite o comprimento do terreno, em metros: '))
calcula_area(largura, comprimento)
