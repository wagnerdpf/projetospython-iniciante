frase = str(input('Digite uma frase: ')).strip().upper()

a = frase.count('A')
a1 = frase.find('A')+1
au = frase.rfind('A')+1

print('A letra A aparece {} vezes'.format(a))
print('A primeira letra A apareceu na posição {}'.format(a1))
print('A última letra apareceu na posição {}'.format(au))
