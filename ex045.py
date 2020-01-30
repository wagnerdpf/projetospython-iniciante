from random import choice
from time import sleep

print('''Escolha:
 [ 1 ] Pedra 
 [ 2 ] Papel
 [ 3 ] Tesoura ''')
humano = int(input('Qual sua escolha? '))

pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'
lista = [pedra, papel, tesoura]
computador = choice(lista)

print('Computador está pensando.......')
sleep(1)
print('O computador escolheu {}'.format(computador))

if computador == pedra and humano == 2:
    print('o Humano ganhou!')
elif computador == papel and humano == 3:
    print('O humano ganhou!')
elif computador == tesoura and humano == 1:
    print('O humano ganhou!')
elif humano == 1 and computador == papel:
    print('O computador ganhou!')
elif humano == 2 and computador == tesoura:
    print('O computador ganhou!')
elif humano == 3 and computador == pedra:
    print('O computador ganhou!')
else:
    print('Deu empate!!!')






