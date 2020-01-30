v = float(input('Digite um valor em metros(m):'))
cm = v*100
mm = v*1000
km = v/1000
hm = v/100
dam = v/10
dm = v*10


print('Esse valor convertido em centímetros é: {:.3f}cm  \nEm milímetros é {:.3f}mm'.format(cm, mm))
print('Esse valor convertido em kilometros é {:.3f}km \nEm hm é {:.3f}hm \nEm dam é {:.3f}dam \nEm dm é{:.3f}dm'.format(km,hm,dam,dm))