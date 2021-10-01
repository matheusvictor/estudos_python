numero = int(input('Digite um número inteiro a ser convertido: '))
print('''Hum...OK! Temos essas opções:
[1] - Convertar para \033[1;32mBINÁRIO\033[m
[2] - Convertar para \033[1;33mOCTAL\033[m
[3] - Convertar para \033[1;34mHEXADECIMAL\033[m
[0] - \033[1;31mEncerrar programa\033[m''')
opcao = int(input('Digite uma das oções acima: '))

if(opcao == 0):
    print('\033[1;31mPrograma encerrado!\033[m')
    exit()
elif(opcao == 1):
    print(f'O número {numero} em \033[1;32mBINÁRIO\033[m é igual a: {bin(numero)}')
elif(opcao == 2):
    print(f'O número {numero} em \033[1;33mOCTAL\033[m é igual a: {oct(numero)}')
elif(opcao == 3):
    print(f'O número {numero} em \033[1;34mHEXADECIMAL\033[m é igual a: {hex(numero)}')
else:
    print('\033[1;31mOpção inválida!\033[m')
