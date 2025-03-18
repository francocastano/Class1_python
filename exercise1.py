"""""

Ejercicio 1

Pruebe las siguientes expresiones en Python. Observe qué resultados obtiene.
Verifique, usando `type()` el tipo de la expresión.


a = 0
b = 1.5 * 0
c = 11 / 2
d = 11 // 2
e = 11.0 // 2.0
f = 2 ** 2
g = "a" + "b"
h = "a" * 0
"""""

a = 0
print(a)
print(type(a))
# retorna un numero entero
b = 1.5 * 0
print(b)
print(type(b))
# retona un float
c = 11 / 2
print(c)
print(type(c))
# retorna un float
d = 11 // 2
print(d)
print(type(d))
# retorna un entero
e = 11.0 // 2.0
print(e)
print(type(e))
# retorna un float
f = 2 ** 2
print(f)
print(type(f))
# retorna un entero
g = "a" + "b"
print(g)
print(type(g))
# concatena el primer string con el segundo string y retona un string
h = "a" * 0
print(h)
print(type(h))