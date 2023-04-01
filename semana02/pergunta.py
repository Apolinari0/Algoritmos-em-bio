s = input("Continuar (s/n)?\n")
while True:
    if s.lower() == 's':
        s = input("Continuar (s/n)?\n")
    elif s.lower() == 'n':
        print("OK, parando...\n")
        break
    else:
        print ("Erro...\n")
        s = input("Continuar (s/n)?\n")