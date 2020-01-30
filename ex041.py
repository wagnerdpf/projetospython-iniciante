from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))

idade = date.today().year - ano

if idade <= 9:
    print('O atleta terá {} anos portanto sua categoria será: MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta terá {} anos portanto sua categoria será: INFATIL'.format(idade))
elif idade <= 19:
    print('O atleta terá {} anos portanto sua categoria será: JUNIOR'.format(idade))
elif idade <= 25:
    print('O atleta terá {} anos portanto sua categoria será: SÊNIOR'.format(idade))
elif idade >= 26:
    print('O atleta terá {} anos portanto sua categoria será: MASTER'.format(idade))

