
# El primer grupo de funciones de módulo math están relacionadas con trigonometría:

# sin(x) → el seno de x.
# cos(x) → el coseno de x.
# tan(x) → la tangente de x.
# Todas estas funciones toman un argumento (una medida de ángulo expresada en radianes) y devuelven el resultado apropiado (ten cuidado con tan() - no todos los argumentos son aceptados).

# Por supuesto, también están sus versiones inversas:

# asin(x) → el arcoseno de x.
# acos(x) → el arcocoseno de x.
# atan(x) → el arcotangente de x.
# Estas funciones toman un argumento (verifican que sea correcto) y devuelven una medida de un ángulo en radianes.


# Para trabajar eficazmente con mediciones de ángulos, el módulo math proporciona las siguientes entidades:

# pi → una constante con un valor que es una aproximación de π.
# radians(x) → una función que convierte x de grados a radianes.
# degrees(x) → una función que convierte x de radianes a grados.
# Ahora observa el código en el editor. El programa de ejemplo no es muy sofisticado, pero ¿puedes predecir sus resultados?


# Además de las funciones circulares (enumeradas anteriormente), el módulo math también contiene un conjunto de sus análogos hiperbólicos:

# sinh(x) → el seno hiperbólico.
# cosh(x) → el coseno hiperbólico.
# tanh(x) → la tangente hiperbólico.
# asinh(x) → el arcoseno hiperbólico.
# acosh(x) → el arcocoseno hiperbólico.
# atanh(x) → el arcotangente hiperbólico.

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)


# Existe otro grupo de las funciones math relacionadas con la exponenciación:

# e → una constante con un valor que es una aproximación del número de Euler (e).
# exp(x) → encontrar el valor de ex.
# log(x) → el logaritmo natural de x.
# log(x, b) → el logaritmo de x con base b.
# log10(x) → el logaritmo decimal de x (más preciso que log(x, 10)).
# log2(x) → el logaritmo binario de x (más preciso que log(x, 2)).
# Nota: la función pow():

# pow(x, y) → encuentra el valor de xy (toma en cuenta los dominios).
# Esta es una función incorporada y no se tiene que importar.

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

# El último grupo consta de algunas funciones de propósito general como:

# ceil(x) → devuelve el entero más pequeño mayor o igual que x.
# floor(x) → el entero más grande menor o igual que x.
# trunc(x) → el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).
# factorial(x) → devuelve x! (x tiene que ser un valor entero y no negativo).
# hypot(x, y) → devuelve la longitud de la hipotenusa de un triángulo rectángulo con las longitudes de los catetos iguales a (x) y (y) (lo mismo que sqrt(pow(x, 2) + pow(y, 2)) pero más preciso).
# Observa el código en el editor. Analiza el programa cuidadosamente.

# Demuestra las diferencias fundamentales entre ceil(), floor() y trunc().

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))
