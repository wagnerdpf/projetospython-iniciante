nome = str(input('Digite seu nome completo: ')).strip()

maisc = nome.upper()
print('Seu nome em letras maisculas: {}'.format(maisc))

min = nome.lower()
print('Seu nome em letras minusculas: {}'.format(min))

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

primeiraletra = nome.split()
print('O numero de letras no primeiro nome é de: {}'.format(len(primeiraletra[0])))