s = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        s += num
        cont = cont + 1
print('Foi informado {}  numeros pares e a soma deles = {}'.format(cont, s))



