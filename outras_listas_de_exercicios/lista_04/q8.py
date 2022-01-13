# -*- coding: utf-8 -*-

# importando módulo datetime
from datetime import datetime

# armazena informações da data (ano, mês, hora, etc) do método now() na variável dataInfo
dataInfo = datetime.now()

nomeEmpregado = raw_input("Nome do(a) empregado(a): ")

while(True):
    anoNasc = int(input("Digite o ano de nascimento do(a) empregado(a): "))

    # se ano de nascimento do func. for maior que ano atual...
    if(anoNasc > dataInfo.year):
        print ("O ano de nascimento não pode ser maior do que o ano atual!\n")
    else:
        break

while(True):
    anoIngresso = int(input("Digite o ano em que o(a) empregado(a) ingressou na empresa: "))

    # se ano de ingresso for maior que ano atual...
    if(anoIngresso > dataInfo.year):
        print ("Ano de ingresso não pode ser maior do que o ano atual!\n")
    else:
        break

idadeEmpregado = dataInfo.year - anoNasc
tempoServico = dataInfo.year - anoIngresso

if(idadeEmpregado >= 65 or tempoServico >= 30 or (idadeEmpregado >=60 and tempoServico >= 25)):
    print("\nNome: {0}\nIdade: {1}\nTempo de serviço: {2} ano(s)\nRequer aposentadoria!".format(nomeEmpregado, idadeEmpregado, tempoServico))
else:
    print("\nNome: {0}\nIdade: {1}\nTempo de serviço: {2} ano(s)\nNão requer aposentadoria!".format(nomeEmpregado, idadeEmpregado, tempoServico))