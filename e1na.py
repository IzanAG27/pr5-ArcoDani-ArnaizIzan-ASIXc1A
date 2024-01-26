"""
    Noms: Daniel Arco, Izan Arnáiz.
    Grup: ASIXc1A
    Data: 26/01/2024
    Descripció:
    Escriure un programa que llegeixi des del teclat dos nombres enters positius
    n1 i n2, amb n1 < n2, i escrigui, començant des de n1, tots els nombres
    enters que són múltiples de n1 més petits o iguals que n2, en ordre creixent.
"""

n1 = int(input(""))
n2 = int(input(""))
multiplos = []


for x in range(n1, n2 + 1):
    if x % n1 == 0:
        multiplos.append(n1)
print(f"Los multiplos de {n1} entre {n1} y {n2} son:  {multiplos}")

