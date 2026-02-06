nome = str(input("Crie um nome de usuário\n:"))

usuario = str(input("Qual o seu usuário?\n:"))

if usuario == nome:
    print("Olá {}, é um prazer lhe conhecer!".format(usuario))
else:
    print("Tente novamente mais tarde {}!".format(usuario))