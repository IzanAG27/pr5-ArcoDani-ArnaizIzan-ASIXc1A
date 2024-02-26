# Variables
LONGUITUD = 333
palabras = [''] * LONGUITUD
paraulesPetites = []
mitjana = 0
indice = 0
numPalabras = 0
continuar = True
print(palabras)
palabra = ""
# Control de errores
while indice < len(palabras) and continuar:
    palabra = input("Introduce una palabra o el símbolo '\\q' para salir): ")
    numPalabras += 1
    mitjana += len(palabra)
    if palabra == "\\q":
        continuar = False
    else:
        palabras[indice] = palabra
        indice += 1

# Creamos una tupla a partir de una lista
tupla_palabras_longitudes = tuple((palabra, len(palabra)) for palabra in palabras if palabra)
print("\nTupla con palabras y medias:")
print(tupla_palabras_longitudes)
print("\nLa mitjana de totes les paraules es:", mitjana // (numPalabras - 1))

# Copiamos las palabras mas pequeñas que la media a una lista
for palabra in palabras:
    if palabra:
        if len(palabra) < (mitjana // (numPalabras - 1)):
            paraulesPetites.append(palabra)
print(paraulesPetites)
