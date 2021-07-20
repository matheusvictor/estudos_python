numero = float(input('Digite um valor em metros para obter sua conversão em cm e mm: '))
cm = numero*100
mm = numero*1000
print('{}m equivale a {:.1f}cm ou {:.1f}mm!'.format(numero, cm, mm))
