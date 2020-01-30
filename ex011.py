h = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
área = h*l
tinta = (h*l)/2
print('A área do cômodo será de {:.2f} m2'. format(área))
print('Considerando que cada litro de tinta pinta uma área de 2m2, esse cômodo irá precisar de {:.2f} litros de tinta'.format(tinta))
