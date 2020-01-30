a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('\33[4;36mÉ possível\33[m fazer um triangulo')
else:
    print('\33[1;31mNão\33[m é possível fazer um triângulo')
