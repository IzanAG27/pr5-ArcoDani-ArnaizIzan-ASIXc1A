"""
    Noms: Daniel Arco, Izan Arnáiz.
    Grup: ASIXc1A
    Data: 22/01/2024
    Descripció:
    Lista de 100 nombres aleatorios entre 1 y 50 y después hacer una media de los nombres pares
    y después de los nombres impares.
"""
import random

nums = [random.randint(1,50) for x in range(100)]
sumaParell = 0
sumaSenar = 0
nombreParell = 0
nombreSenar = 0

for i in range(0, 99):
    if nums[i] % 2 == 0:
        sumaParell += nums[i]
        nombreParell += 1
    else:
        sumaSenar += nums[i]
        nombreSenar += 1
print(f"La mitjana dels números parells es: {sumaParell // nombreParell}.")
print(f"La mitjana dels números senars es: {sumaSenar // nombreSenar}.")