s = 0
cont = 0
for n in range(1, 500, 2):
    if n % 3 == 0:
        s += n
        cont = cont + 1
print('A soma entre os numeros ímpares que são múltiplos de três (são {} valores) no intervalo de 1 até 500 = {} '.format(cont, s))




