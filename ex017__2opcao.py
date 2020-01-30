from math import hypot

b = float(input('Digite o comprimento do cateto oposto: '))
c = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(b,c)
print('O valor da hipotenusa será de: {:.2f}'.format(hi))
