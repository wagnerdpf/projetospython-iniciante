num = int(input('Digite um numero para saber sua tabuada: '))
print('-'*50)
for c in range(1, 11):
    tab = num * c
    print('{} x {:2} = {:2}'.format(num, c, tab))
print('-'*50)



