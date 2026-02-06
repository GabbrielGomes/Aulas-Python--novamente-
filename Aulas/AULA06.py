#tipos primitivos principais

int() # números interios "int" 7, -3, 9482
float() # números com ponto flutuante "float" 4.3, -32.3, 3.14, 4.0
bool() # aceita dois valores "True" ou "False"
str() # tudo que estar entre aspas 'olá', '7.5'

# print("Valor d soma {}".format(s))

n1 = int(input('valor 1: '))
n2 = int(input('Valor 2: '))
s = n1 + n2

print('A soma do {} mais {} é {}!'.format(n1, n2, s))

p = str(input('Digite algo:\n'))

print(p.isalpha)