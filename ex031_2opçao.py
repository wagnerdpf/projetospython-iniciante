dist = float(input('Qual a distância em km de sua viagem? '))

preço = dist * 0.50 if dist <= 200 else dist * 0.45
print('O preço da sua passagem será de R$ {}'.format(preço))
