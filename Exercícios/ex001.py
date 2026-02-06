text = int(input("O que vc quer que apareça no prompt?\n[1] Olá Mundo!\n[2] Hellow world!\n") )

if text != 1 or 2:
    print(text)
    
if text == 1:
    print("Olá Mundo!")