valor_produto = int(input('Qual o valor do seu produto para calcularmos o desconto de 5%? '))

desconto = valor_produto * (5/100)

valor_desconto = valor_produto - desconto

print('O valor de R${} com 5% de desconto fica no valor de R${}'.format(valor_produto, valor_desconto))
