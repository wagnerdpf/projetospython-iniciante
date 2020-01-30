from datetime import date
atual = date.today().year
print('Estamos no ano de {}'.format(atual))

anonasc = int(input('Qual o ano de nascimento do jovem? '))

if (date.today().year - anonasc) < 18:
    tf = 18 - (date.today().year - anonasc)
    print('O jovem ainda terá que se alistar no serviço militar! Faltam {} anos!'.format(tf))
    ano = atual + tf
    print('Seu alistamento será no ano de {}'. format(ano))
elif (date.today().year - anonasc) == 18:
    print('Está na hora de se alistar!')
elif (date.today().year - anonasc) > 18:
    tp = (date.today().year - anonasc) - 18
    print('Já passou {} anos do prazo para alistamento!!!'.format(tp))
    ano = atual - tp
    print('O alistamento teria que ter sido feito em {}'.format(ano))








