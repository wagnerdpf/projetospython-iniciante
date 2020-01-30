import math

b = float(input('Digite o comprimento do cateto oposto: '))
c = float(input('Digite o comprimento do cateto adjacente: '))

co = math.pow(b,2)
ca = math.pow(c,2)
h = math.sqrt(co+ca)

print('Sabendo que os comprimentos do catetos são {} e {}, a hipotenusa será de {:.2f}'.format(co,ca,h))

