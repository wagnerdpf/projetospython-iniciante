from math import radians, sin, cos, tan

a = float(input('Digite o valor de um ângulo: '))

sen = sin((radians(a)))
cos = cos((radians(a)))
tan = tan((radians(a)))

print('O valor do seno é {:.2f}, do cosseno é {:.2f} e da tangente é {:.2f}'.format(sen, cos, tan))