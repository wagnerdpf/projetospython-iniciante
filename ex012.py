p = float(input('Quanto custa o produto? R$ '))
np = p - (p * 5 / 100)
print('Com o desconto de 5% o preço final desse produto será de R$ {:.2f}'.format(np))