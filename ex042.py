a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('É possível fazer um triangulo!')
    if a == b == c:
       print('É um triangulo equilatero')
    elif a != b != c != a:
       print('É um triangulo escaleno')
    else:
       print('É um triangulo isóscles')
else:
    print('Não é possível fazer um triangulo!')


