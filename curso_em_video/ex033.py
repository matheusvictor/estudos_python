primeiro_numero = input("Digite o 1º número: ")
segundo_numero = input("Digite o 2º número: ")
terceiro_numero = input("Digite o 3º número: ")

maior_numero = primeiro_numero
menor_numero = primeiro_numero

#verificando maior número:
if(segundo_numero > primeiro_numero and segundo_numero > terceiro_numero):
    maior_numero = segundo_numero
elif(terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero):
    maior_numero = terceiro_numero

#verificando menor número:
if(segundo_numero < primeiro_numero and segundo_numero < terceiro_numero):
    menor_numero = segundo_numero
elif(terceiro_numero < primeiro_numero and terceiro_numero < segundo_numero):
    menor_numero = terceiro_numero

print(f'{maior_numero} é o maior número digitado e {menor_numero} é o menor.')
