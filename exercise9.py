"""
Ejercicio 9

Escriba un programa que permita al usuario ingresar el valor de dos variables
numéricas de tipo entero. Posteriormente, el programa debe intercambiar los
valores de ambas variables y mostrar el resultado final por pantalla. Por
ejemplo, si el usuario ingresa los valores num1 = 9 y num2 = 3, la salida del
programa deberá mostrar: num1 = 3 y num2 = 9.

Ayuda: Para intercambiar los valores de dos variables se debe utilizar una
variable auxiliar.
"""

num1 = int(input())
num2 = int(input())
aux = num1
num1 = num2 
num2 = aux
#num1,num2 = num2,num1
# print("num1 = ", num1,"num2 = ", num2)
print(f"num1 = {num1}", f"num2 = {num2}")