continuar = True
while continuar:
    cadena = str(input(""))
    cadena = cadena.lower()
    if cadena == "eso es todo amigos":
        continuar = False
    else:
        for x in range(len(cadena)):
            if cadena[x] == "a" or cadena[x] == "á" or cadena[x] == "à":
                print("1", end="")
            elif cadena[x] == "e" or cadena[x] == "é" or cadena[x] == "è":
                print("2", end="")
            elif cadena[x] == "i" or cadena[x] == "í" or cadena[x] == "ì":
                print("3", end="")
            elif cadena[x] == "o" or cadena[x] == "ó" or cadena[x] == "ò":
                print("4", end="")
            elif cadena[x] == "u" or cadena[x] == "ú" or cadena[x] == "ù":
                print("5", end="")
            else:
                print(cadena[x], end="")
        print("")