from random import choice

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

alunos = [a1, a2, a3, a4]

s = choice(alunos)

print('Entre os alunos {}, {}, {} e {}, o escolhido para apagar a lousa foi: {}'.format(a1, a2, a3, a4, s))

