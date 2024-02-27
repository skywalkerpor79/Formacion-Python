# import math

# x = float(input("Ingresa x: "))
# y = math.sqrt(x)

# print("La raíz cuadrada de", x, "es igual a", y)
#################
# first_number = int(input("Ingresa el primer numero: "))
# second_number = int(input("Ingresa el segundo numero: "))

# try:
#     print(first_number / second_number)
# except:
#     print("Esta operación no puede ser realizada.")

# print("FIN.")
###############
# try:
#     x = int(input("Ingresa un numero: "))
#     y = 1 / x
#     print(y)
# except ZeroDivisionError:
#     print("No puedes dividir entre cero, lo siento.")
# except ValueError:
#     print("Debes ingresar un valor entero.")
# except:
#     print("Oh cielos, algo salió mal...")

# print("FIN.")
#############
# try:
#     y = 1 / 0
# except ArithmeticError:
#     print("Uuuppsss...")

# print("FIN.")

# try:
#     y = 1 / 0
# except ZeroDivisionError:
#     print("Uuuppsss...")

# print("FIN.")
##############
# try:
#     y = 1 / 0
# except ZeroDivisionError:
#     print("¡División entre Cero!")
# except ArithmeticError:
#     print("¡Problema Aritmético!")

# print("FIN.")

# try:
#     y = 1 / 0
# except ArithmeticError:
#     print("¡Problema Aritmético!")
# except ZeroDivisionError:
#     print("¡División entre Cero!")

# print("FIN.")
##########
# La sentencia de Python raise ExceptionName puede generar una excepción bajo demanda. La misma sentencia pero sin ExceptionName, se puede usar solamente dentro del bloque try, y genera la misma excepción que se está manejando actualmente.

# def bad_fun(n):
#     raise ZeroDivisionError

# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("¿Que pasó? ¿Un error?")

# print("FIN.")
#########

# def bad_fun(n):
#     try:
#         return n / 0
#     except:
#         print("¡Lo hice otra vez!")
#         raise

# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("¡Ya veo!")
# print("FIN.")
#####
# La sentencia de Python assert expression evalúa la expresión y genera la excepción AssertError cuando la expresión es igual a cero, una cadena vacía o None. Puedes usarla para proteger algunas partes críticas de tu código de datos devastadores.
import math

x = float(input("Ingresa un número: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)
