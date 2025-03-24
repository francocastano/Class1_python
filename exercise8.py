"""
Ejercicio 8

Escribir un programa que calcule cuántos litros de combustible consumió un automóvil. El usuario debe
ingresar una cantidad de litros de combustible cargados en la estación y una cantidad de kilómetros
recorridos. Después, el programa calculará el consumo (km/lt) y se lo mostrará al usuario.
"""

fuel = float(input("ingrese cantidad de combustible cargado"))
distance = float(input("ingrese cantidad de kilomtros recorridos"))

consume = distance/fuel

print("El consunmo fue de", consume, "km por litro") 