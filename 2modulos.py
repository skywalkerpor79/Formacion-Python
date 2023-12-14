# Importamos todo el modulo de math
# import math

# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None


# pi = 3.14

# print(sin(pi/2))
# print(math.sin(math.pi/2))

# Importamos solo la entidad pi i sin del modulo math
from math import sin, pi
print(sin(pi/2))

# Par importarlo todo pero tendremos conflictos de nombres seguramente i no es recomendable
# from module import *
# si no nos gusta el nombre del modulo lo canviamos con as
# import module as alias
# from math import pi as PI, sin as sine

import math

for name in dir(math):
    print(name, end="\t")



