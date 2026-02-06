# +: adição                    #ORDEM DE PRECEDENCIA
# -: subtração                 # 1ª ()
# *: multiplicação             # 2ª **
# /: divisão                   # 3ª *, /, //, %
# **: potencia                 # 4ª +, -
# //: divisão inteira
# %: resto da divisão
# ==: igual a

print('='*20)
print('oi'*5)

n1 = int(input('Valor um: '))
n2 = int(input('Valor dois: '))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1 ** n2 
d_inteira = n1 // n2
r_divisao = n1 % n2

print('A soma vale {}\nA subtração vale {}\nA multiplicação vale {}' \
'\nA divisao vale {}\nA potência vale {}\nA divisão inteira vale {}' \
'\nE o resto da divisão é {}'.format(soma, subtracao, multiplicacao, divisao,
                                      potencia, d_inteira, r_divisao))

print('A soma vale {}!'.format(n1+n2))
