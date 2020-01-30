vel = float(input('Qual é a velocidade do seu carro: '))

if vel > 80:
    print('Você ultrapassou a velocidade limite de 80 km/h e foi\33[1;31m MULTADO\33[m!!!')
    multa = (vel - 80) * 7
    print('Terá que pagar  R$ {:.2f} reais de multa!'.format(multa))
print('Tenha um bom dia, dirija com segurança!')

