nome = str(input('Digite um nome: ')).strip()

n = 'SILVA' in nome.upper()

print('No nome digitado aparece \33[1;35;40mSilva\33[m: {}'.format(n))