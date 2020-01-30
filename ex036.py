valor = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual salário do comprador? R$ '))
anos = int(input('Em quantos anos será pago? '))

parcelas = (valor / anos) / 12
parsal = salario * (30 / 100)

print('De acordo com as informações dadas o valor das prestações mensais serão de R$ {:.2f}'.format(parcelas))

if parcelas <= parsal:
    print('O empréstimo foi \033[1;34mAPROVADO\033[m!!!')
else:
    print('O empréstimo será \033[1;31mNEGADO\033[m!!!')