import random
from time import sleep

num = random.randint(0,5)

print('O computador está pensando em um numero de 0 a 5. Tente adivinhar...')

numusuario = int(input('Em que numero o computador está pensando? '))
print('\33[1;30mPROCESSANDO...\33[m')
sleep(2)

if numusuario == num:
    print('O usuário \33[1;34;40mvenceu!!!\33[m')
else:
    print('O computador pensou no numero {} e o usuário escolheu o numero {}, portanto o usuário\33[1;31;43m perdeu\33[m!!!'.format(num, numusuario))
