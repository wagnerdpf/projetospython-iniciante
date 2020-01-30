print('{:=^40}'.format(' LOJA DO WAGNER '))
preço = float(input('Digite o preço do produto: R$ '))
print(''' Escolha uma opção de pagamento:
[1] à vista dinheiro/cheque:10% de desconto
[2] à vista no cartão:5% de desconto
[3] em até 2x no cartão:preço normal
[4] 3x ou mais no cartão:20% de juros''')
opção = int(input('Escolha a opção de pagamento: '))

if opção == 1:
    pf = preço - (preço * 10 / 100)
    print('O valor a ser pago será de R$ {:.2f}'.format(pf))
elif opção == 2:
    pf = preço - (preço * 5 / 100)
    print('O valor a ser pago será de R$ {:.2f}'.format(pf))
elif opção == 3:
    p = preço / 2
    print('O valor será parcelado em 2x sem juros de R$ {}'.format(p))
elif opção == 4:
    np = int(input('Quantas parcelas? '))
    pf = preço + (preço * 20 / 100)
    p = pf / np
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros e no final o valor total a ser pago será de R$ {:.2f} '.format(np,p,pf))
else:
    print('Escolha uma opção válida de pagamento!')





