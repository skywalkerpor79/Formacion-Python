# Funciones seleccionadas del módulo platform
# La función platform

# El módulo platform permite acceder a los datos de la plataforma subyacente, es decir, hardware, sistema operativo e información sobre la versión del intérprete.

# Existe también una función que puede mostrar todas las capas subyacentes en un solo vistazo, llamada platform. Simplemente devuelve una cadena que describe el entorno; por lo tanto, su salida está más dirigida a los humanos que al procesamiento automatizado (lo verás pronto).

# Así es como se puede invocar:

# platform(aliased = False, terse = False)


# Y ahora:

# aliased → cuando se establece a True (o cualquier valor distinto a cero) puede hacer que la función presente los nombres de capa subyacentes alternativos en lugar de los comunes.
# terse → cuando se establece a True (o cualquier valor distinto a cero) puede convencer a la función de presentar una forma más breve del resultado (si lo fuera posible).



from platform import platform
platform(aliased = False, terse = False)
print(platform())
print(platform(1))
print(platform(0, 1))

# La función machine

# En ocasiones, es posible que solo se desee conocer el nombre genérico del procesador que ejecuta el sistema operativo junto con Python y el código, una función llamada machine() te lo dirá. Como anteriormente, la función devuelve una cadena.

from platform import machine

print(machine())

# La función processor

# La función processor() devuelve una cadena con el nombre real del procesador (si lo fuese posible).

from platform import processor

print(processor())

# La función system

# Una función llamada system() devuelve el nombre genérico del sistema operativo en una cadena.

from platform import system

print(system())

# La función version

# La versión del sistema operativo se proporciona como una cadena por la función version().

from platform import version

print(version())

# Las funciones python_implementation y python_version_tuple

# Si necesitas saber que versión de Python está ejecutando tu código, puedes verificarlo utilizando una serie de funciones dedicadas, aquí hay dos de ellas:

# python_implementation() → devuelve una cadena que denota la implementación de Python (espera CPython aquí, a menos que decidas utilizar cualquier rama de Python no canónica).
# python_version_tuple() → devuelve una tupla de tres elementos la cual contiene:
# La parte mayor de la versión de Python.
# La parte menor.
# El número del nivel de parche.

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

#