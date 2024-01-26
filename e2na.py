"""
    Noms: Daniel Arco, Izan Arnáiz.
    Grup: ASIXc1A
    Data: 26/01/2024
    Descripció:
    Programa que calcula la suma dels dígits parells d'un número positiu.
"""

num = input("")
suma = 0
for x in range(len(num)):
    if int(num[x]) % 2 == 0:
        suma += int(num[x])
print(suma)