"""
Ejercicio 10

Modelar los siguientes problemas, nombrando los datos relevantes de entrada y
salida, junto con los tipos de datos que se usarán para representarlos dentro de
Python. Luego programar la solución.

a) Se tienen dos habitaciones dentro de un hogar, cada una con una temperatura
   ambiente posiblemente distinta.
Se quiere saber a qué temperatura estarán las habitaciones, dado suficiente
tiempo para que se transmita el calor de una a la otra.

b) Se tiene una multitud afuera, cada persona le dirá su nombre a cada otra
   persona en la multitud.
Se quiere saber cuánto tiempo llevará hacer esto, dado que decir una vez tu
nombre lleva aproximadamente 4 segundos y medio.

c) Hay dos personas con nombres muy largos, pero similares.
Se quiere conocer, por un lado, si tienen el mismo tamaño, y por otro lado si
son iguales.

Ayuda para el programa: investigar la función `len`.
"""
#a
# room1 = float(input())
# room2 = float(input())
# average = (room1+room2)/2
# print(f"El promedio de la temperatura es {average}")
# #b
# say_name = 4.5
# crowd = int(input())
# time_to_say_names = crowd * say_name
# print(time_to_say_names)
#c
name1 = input()
name2 = input()
if name1 == name2:
    print("son el mismo nombre")
elif len(name1) == len(name2):
    print("son del mismo tamaño")
else:
    print("No tienen la misma logitud")