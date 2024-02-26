# Control de errores
try:
    print("--Tip-- Introdueix el número de files, prem intro i després el número de columnes:")
    files = int(input(""))
    columnes = int(input(""))
    # Mismas columnas y filsa
    if files == columnes:
        # Tienen que ser impares
        if files % 2 != 0 and columnes % 2 != 0:
            matriu = [[0] * columnes for x in range(files)]
            for x in range(files):
                for y in range(columnes):
                    if y == 0 or y == files - 1:
                        matriu[x][y] = int(1)
            for x in matriu:
                print(x)
        else:
            print("Los valores de las filas y columnas deben ser impares")
    else:
        print("Introduce las mismas filas que columnas")
except ValueError:
    print("\nIntroduce valores enteros")
finally:
    print("Programa terminado")
