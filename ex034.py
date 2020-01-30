print('Aqueles com salário superior a R$ 1250.00 terão um acréscimo de 10% no salário; salários inferiores ou iguais a esse valor o acréscimo será de 15%')

sal = float(input('Qual o valor do seu salário? R$ '))


a = sal*(10 / 100) + sal
b = sal*(15 / 100) + sal

if sal > 1250:
    print('Seu novo salário com um aumento de\33[7;30m 10% \33[mserá de R$ {:.2f}'.format(a))
else:
    print('Seu novo salário com um aumento de \33[7;30m15% \33[mserá de R$ {:.2f}'.format(b))