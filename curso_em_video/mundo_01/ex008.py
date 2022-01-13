numero = float(input('Digite um valor em metros para obter sua conversão em km, hm, dam, dm, cm e mm: '))

km = numero/1000
hm = numero/100
dam = numero/10
dm = numero*10
cm = numero*100
mm = numero*1000

print(f'{numero}m equivale às conversões abaixo:')
print(f'{km:.3f}km\n{hm:.2f}hm\n{dam:.1f}dam\n{dm:.1f}dm\n{cm:.1f}cm\n{mm:.1f}mm')
