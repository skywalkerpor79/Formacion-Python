# La función random

# La función general llamada random() (no debe confundirse con el nombre del módulo) produce un número flotante x entre el rango (0.0, 1.0) - en otras palabras: (0.0 <= x < 1.0).

# El programa de ejemplo a continuación producirá cinco valores pseudoaleatorios, ya que sus valores están determinados por el valor semilla actual (bastante impredecible), no puedes adivinarlos:

from random import random

for i in range(5):
    print(random())

# La función seed

# La función seed() es capaz de directamente establecer la semilla del generador. Te mostramos dos de sus variantes:

# seed() - establece la semilla con la hora actual.
# seed(int_value) - establece la semilla con el valor entero int_value.
# Hemos modificado el programa anterior; de hecho, hemos eliminado cualquier rastro de aleatoriedad del código:    

# los resultados seran siempre el mismo aleatorio porque con el seed hacemos que la semilla empiece siempre en el mismo sitio
from random import random, seed

seed(0)

for i in range(5):
    print(random())

# Funciones seleccionadas del módulo random: continuación
# Las funciones randrange y randint

# Si deseas valores aleatorios enteros, una de las siguientes funciones encajaría mejor:

# randrange(fin)
# randrange(inico, fin)
# randrange(inicio, fin, incremento)
# randint(izquierda, derecha)
# Las primeras tres invocaciones generarán un valor entero tomado (pseudoaleatoriamente) del rango:

# range(fin)
# range(inicio, fin)
# range(inicio, fin, incremento)
# Toma en cuenta la exclusión implícita del lado derecho.

# La última función es equivalente a randrange(izquierda, derecha+1) - genera el valor entero i, el cual cae en el rango [izquierda, derecha] (sin exclusión en el lado derecho).

# Observa el código en el editor. Este programa generará una línea que consta de tres ceros y un cero o un uno en el cuarto lugar.

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

# Las funciones choice y sample

# Como puedes ver, esta no es una buena herramienta para generar números para la lotería. Afortunadamente, existe una mejor solución que escribir tu propio código para verificar la singularidad de los números "sorteados".


# Es una función con el nombre de choice:

# choice(secuencia)
# sample(secuencia, elementos_a_elegir=1)
# La primera variante elige un elemento "aleatorio" de la secuencia de entrada y lo devuelve.

# El segundo crea una lista (una muestra) que consta del elemento elementos_a_elegir (que por defecto es 1) "sorteado" de la secuencia de entrada.

# En otras palabras, la función elige algunos de los elementos de entrada, devolviendo una lista con la elección. Los elementos de la muestra se colocan en orden aleatorio. Nota que elementos_a_elegir no debe ser mayor que la longitud de la secuencia de entrada.
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))
