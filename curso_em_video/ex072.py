numeros_extensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numeral = -1
while(numeral < 0 or numeral > 20):
    numeral = int(input('Digite um número entre 0 e 20: '))

print(f'Você digitou o número {numeros_extensos[numeral]}.')
