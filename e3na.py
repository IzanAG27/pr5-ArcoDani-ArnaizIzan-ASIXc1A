"""
    Noms: Daniel Arco, Izan Arnáiz.
    Grup: ASIXc1A
    Data: 26/01/2024
    Descripció:
    Programa que determina si un valor es múltiple de 2 i/o si es múltiple de 5..
"""

try:
    valor = int(input(""))

    if valor % 2 == 0 and valor % 5 == 0:
        print("Múltiple de 2 i 5")
    elif valor % 2 == 0:
        print("Múltiple de 2")
    elif valor % 5 == 0:
        print("Múltiple de 5")
    else:
        print("Error, el valor introduït no es múltiple de 2 i/o 5\n")
except ValueError:
    print("Error, introduce un valor entero positivo.")
finally:
    print("\nPrograma terminado")