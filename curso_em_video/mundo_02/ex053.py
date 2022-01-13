frase = str(input('Digite uma frase: ')).lower()
frase_sem_espacos = frase.replace(' ', '') # substitui os espaços por nenhum espaço
frase_invertida = frase_sem_espacos[::-1]

if(frase_sem_espacos == frase_invertida):
    print(f'A frase "{frase}" é um palíndromo!')
else:
    print(f'A frase "{frase}" NÃO é um palíndromo!')
