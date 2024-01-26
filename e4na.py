"""
    Noms: Daniel Arco, Izan Arnáiz.
    Grup: ASIXc1A
    Data: 26/01/2024
    Descripció:
    10 preus i calcula la mitjana dels preus i el preu mes elevat.
"""

preu = [int(x) for x in input("").split()]
preusIntroduits = []
PreusSorted = []
suma = 0
if len(preu) == 10:
    for x in preu:
        preusIntroduits.append(x)
        suma += x
    PreusSorted = sorted(preusIntroduits)
    print(f"La mitjana es: {suma // 10}.\nEl preu mes elevat es: {PreusSorted[-1:]}."
          f"\nAquest son els preus introduïts: {preusIntroduits}")