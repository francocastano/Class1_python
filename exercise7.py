"""
Ejercicio 7

Conocido el número en matemática PI, pedir al usuario que ingrese el valor del radio de una circunferencia y calcular y mostrar por pantalla el área y perí́metro. Recuerde que para calcular el área y el perí́metro se utilizan las siguientes fórmulas:

Area = π * radio^2
Perimetro = 2 * π * radio
"""

from math import pi

radio = float(input("ingrese el radio de la circunferencia:"))
print(radio)

area = pi * radio**2
per = 2* pi * radio

print("El area es:", area,"y el perimetro es", per)