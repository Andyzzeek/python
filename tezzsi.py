def Prihlaseni(jmeno = input("jmeno:"),parek = input("heslo:")):
    if jmeno == "admin":
        print("Ahoj Admine")
    elif jmeno == "student":
        print("Ahoj Studente")
    else:
        print("Neopravneny login, ktery bude nahlasen.")


Prihlaseni()