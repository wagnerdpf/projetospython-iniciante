d = int(input('Quantos dias alugados? '))
km = float(input('Quantos kilometros rodados? '))

tp = (d * 60) + (km * 0.15)



print('Considerando que o custo diário do aluguel é de R$60,00 e cada kilometro custa R$ 0.15, O total a pagar será de R$ {:.2f}'.format(tp))
