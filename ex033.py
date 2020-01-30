a = int(input('Digite um primeiro valor: '))
b = int(input('Digite um segundo valor: '))
c = int(input('Digite um terceiro valor: '))

#Verificando o menor
menor = a
if b < a and b < c:
   menor = b
if c < a and c < b:
    menor = c
print('O menor valor será: {}'.format(menor))

#Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor será: {}'.format(maior))