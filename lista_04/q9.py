# -*- coding: utf-8 -*-

jornadaSemanalTrabalho = 40
numeroSemanas = 4
acrescimo = 0.50

horasTrabalhadasMes = input("Digite o número de horas trabalhadas durante o mês: ")
valorHora = input("Informe valor ganho por hora: R$")

horasTrabalhadasSemana = horasTrabalhadasMes / numeroSemanas
horasExtrasSemana = horasTrabalhadasSemana - jornadaSemanalTrabalho
horasExtrasMes = horasExtrasSemana * numeroSemanas

salarioMes = (horasTrabalhadasMes - horasExtrasMes) * valorHora

if(horasTrabalhadasSemana > 40):

    valorHoraExtra = valorHora + (valorHora * acrescimo)
    
    salarioExtraMes = valorHoraExtra * horasExtrasMes

    salarioMes = salarioMes + salarioExtraMes

print("\nHoras trabalhadas no mês: {0}h".format(horasTrabalhadasMes))
print("Horas trabalhadas por semana: {0}h".format(horasTrabalhadasSemana))
print("Horas extra por semana: {0}h".format(horasExtrasSemana))
print("Horas extra por mês: {0}h".format(horasExtrasMes))
print("Salário Extra: R${0}".format(salarioExtraMes))
print("Salário: R${0}".format(salarioMes))
