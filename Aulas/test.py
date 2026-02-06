n1 = int(input("QUal o primeiro valor? "))
n2 = int(input("Qual o segundo valor? "))

op = int(input("Qual operação deseja realizar? \n [1]Soma \n [2]Subtração \n"))

soma = n1 + n2
subtração = n1 - n2

if op == 1:
    print("A soma dos dois números são", soma)

if op == 2:
    print("A subtração dos dois números são", subtração)

