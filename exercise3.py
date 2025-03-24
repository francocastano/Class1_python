"""
Ejercicio 3

Encontrar el resultado que devuelven las siguientes expresiones
"""
a = (4 >= 40 and 8 <= 10) or (2 < 20 or 10 > 100)
#true
b = 5 <= 10 or (2 / 0) == 1
#true
c = (8 >= 10 or 4 <= 8) and (3 != 10 or 10 >= 4)
#true
d = (50 > 49 and 7 == 5) or (15 <= 14 or 10 > 100)
#false
e = not(not(10 >= 8) and 1 > 3) or (2 != 3 and 2 < 8)
#true
f = (4 > 2 or 7 > 6) and not(3 < 6 or 2 > 0)
#false
g = not(0)
#true
h = not(1)
#false
i = not(8)
#false
j = not('a')
#true
k = not([])
#true
l = not('') or not(' ')
#true
