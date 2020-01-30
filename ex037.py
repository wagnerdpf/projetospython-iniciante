num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
opcao = int(input('Sua opção: '))

if opcao ==1:
    print(bin(num)[2:])
elif opcao==2:
    print(oct(num)[2:])
elif opcao==3:
    print(hex(num)[2:])
else:
    print('Opção inexistente!!!')

