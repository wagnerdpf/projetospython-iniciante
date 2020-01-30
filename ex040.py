nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('O aluno está \033[1;31mreprovado\033[m!')
elif 7 > media >= 5:
    print('O aluno está de \033[1;32mrecuperação\033[m')
elif media >= 7:
    print('O aluno está \033[1;34maprovado\033[m')


