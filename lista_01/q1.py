# -*- coding: utf-8 -*-

a = 10
b = 20

# verifica os atuais valores atribuídos às variáveis 'a' e 'b'
print(a, b)

# A variável 'aux' irá guardar o antigo valor de 'a'
aux = a
# 'a' receberá o valor de 'b'. Neste caso, o valor recebido por 'a' será 20
a = b
# 'b' irá receber o antigo valor de 'a', que foi guardado na varivável 'aux'
b = aux

# verifica se os valores de 'a' e 'b' foram trocados
print(a, b)