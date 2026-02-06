largura = int(input('Qual a largura da sua parede? '))
comprimento = int(input('QUal o comprimento da sua parede? '))

metros_quadrados = largura * comprimento

pintura = metros_quadrados / 2

print('Se cada litro de tinta pinta 2m², então, será necessários {}L de tinta para pintar sua parede de {}m²'.format(pintura, metros_quadrados))