dist = float(input('\33[7;30mQual a distância em km de sua viagem? \33[m'))

if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45
print('O preço da passagem será de {:.2f} reais'.format(preço))
