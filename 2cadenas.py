# 1. Algunos de los métodos que ofrecen las cadenas son:

# capitalize(): cambia todas las letras de la cadena a mayúsculas.
# center(): centra la cadena dentro de una longitud conocida.
# count(): cuenta las ocurrencias de un carácter dado.
# join(): une todos los elementos de una tupla/lista en una cadena.
# lower(): convierte todas las letras de la cadena en minúsculas.
# lstrip(): elimina los caracteres en blanco al principio de la cadena.
# replace(): reemplaza una subcadena dada con otra.
# rfind(): encuentra una subcadena comenzando por el final de la cadena.
# rstrip(): elimina los caracteres en blanco al final de la cadena.
# split(): divide la cadena en una subcadena usando un delimitador dado.
# strip(): elimina los espacios en blanco iniciales y finales.
# swapcase(): intercambia las mayúsculas y minúsculas de las letras.
# title(): hace que la primera letra de cada palabra sea mayúscula.
# upper(): convierte todas las letras de la cadena en letras mayúsculas.

# 2. El contenido de las cadenas se puede determinar mediante los siguientes métodos (todos devuelven valores booleanos):

# endswith(): ¿La cadena termina con una subcadena determinada?
# isalnum(): ¿La cadena consta solo de letras y dígitos?
# isalpha(): ¿La cadena consta solo de letras?
# islower(): ¿La cadena consta solo de letras minúsculas?
# isspace(): ¿La cadena consta solo de espacios en blanco?
# isupper(): ¿La cadena consta solo de letras mayúsculas?
# startswith(): ¿La cadena consta solo de letras mayúsculas?


word='by'
print(len(word))

empty=''
print(len(empty))

i_am='I\'m'
print(len(i_am))

multiline='''Línea #1
Línea @2'''

print(len(multiline))
print(multiline)

str1='a'
str2='b'

print(str1+str2)
print(str2+str1)
print(5*'a')
print('b'*4)


# Para saber valor asci, (recordamos que el 32 es espacio en blanco i mas 32 hacen las mayusculas)
char_1='a'
char_2=' '
print(ord(char_1))
print(ord(char_2))

print(chr(97))
print(chr(945))

# Los dos casos es lo mismo
# Indexando cadenas.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

# Iterando a través de una cadena.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()

# Rebanadas

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

# Los operadores in y not in
# El operador in

# El operador in no debería sorprenderte cuando se aplica a cadenas, simplemente comprueba si el argumento izquierdo (una cadena) se puede encontrar en cualquier lugar dentro del argumento derecho (otra cadena).

# El resultado es simplemente True(Verdadero) o False(Falso).

# Observa el ejemplo a continuación. Así es como el operador in funciona:

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet, end='\n\n')

# El operador not in

# Como probablemente puedas deducir, el operador not in también es aplicable aquí.

# Así es como funciona:

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

# no hay insert ni del por posicion sino completo ni append, se ha trabajar un poco diferente
alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)

# min nos daria el valor mas bajo (hexadecimal del elemento de la cadena)
# Demonstrando min() - Ejemplo 1:
print(min("aAbByYzZ"))


# Demonstrando min() - Ejemplo 2 y 3:
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))


#lo mismo pero con max
# Demostración de max() - Ejemplo 1:
print(max("aAbByYzZ"))


# Demostración de max() - Ejemplo 2 & 3:
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

print(ord('¡'))

# Operaciones con cadenas: el método index()
# El método index() (es un método, no una función) busca la secuencia desde el principio, para encontrar el primer elemento del valor especificado en su argumento.

# Nota: el elemento buscado debe aparecer en la secuencia - su ausencia causará una excepción ValueError.

# El método devuelve el índice de la primera aparición del argumento (lo que significa que el resultado más bajo posible es 0, mientras que el más alto es la longitud del argumento decrementado en 1).


# Demonstrando el método index():
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))



# Operaciones con cadenas: la función list()
# La función list() toma su argumento (una cadena) y crea una nueva lista que contiene todos los caracteres de la cadena, uno por elemento de la lista.

# Nota: no es estrictamente una función de cadenas - list() es capaz de crear una nueva lista de muchas otras entidades (por ejemplo, de tuplas y diccionarios).

# Demostración de la función list():
print(list("abcabc"))
      
# salida

# Operaciones con cadenas: el método count()
# El método count() cuenta todas las apariciones del elemento dentro de la secuencia. La ausencia de tal elemento no causa ningún problema.

# Demostración de la función list():
print("abcabc".count("b"))
print('abcabc'.count("d"))

# El método capitalize() hace exactamente lo que dice - crea una nueva cadena con los caracteres tomados de la cadena fuente, pero intenta modificarlos de la siguiente manera:

# Si el primer carácter dentro de la cadena es una letra (nota: el primer carácter es el elemento con un índice igual a 0, no es el primer carácter visible), se convertirá a mayúsculas.
# Todas las letras restantes de la cadena se convertirán a minúsculas.

# Demostración del método capitalize():
print('aBcD'.capitalize())

#  método center() genera una copia de la cadena original, tratando de centrarla dentro de un campo de un ancho especificado.
# El centrado se realiza realmente al agregar algunos espacios antes y después de la cadena.
# No esperes que este método demuestre habilidades sofisticadas. Es bastante simple.
# El ejemplo en el editor usa corchetes para mostrar claramente donde comienza y termina realmente la cadena centrada
# Demostración del método center():
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(5) + ']')
print('[' + 'gamma'.center(20, '*') + ']')

# método endswith() comprueba si la cadena dada termina con el argumento especificado y devuelve True(verdadero) o False(falso), dependiendo del resultado.

# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

# El método startswith() es un espejo del método endswith()

# Demostración del método startswith():
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

# El método find() es similar al método index(), el cual ya conoces - busca una subcadena y devuelve el índice de la primera aparición de esta subcadena, pero:
# Es más seguro, no genera un error para un argumento que contiene una subcadena inexistente (devuelve -1 en dicho caso).
# Funciona solo con cadenas - no intentes aplicarlo a ninguna otra secuencia.

# Demostración del método find():
print("Eta".find("ta"))
print("Eta".find("mma"))

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

# rfind() hacen casi lo mismo que sus contrapartes (las que carecen del prefijo r), pero comienzan sus búsquedas desde el final de la cadena, no el principio (de ahí el prefijo r, de reversa).
# Demostración del método rfind():
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# El método sin parámetros llamado isalnum() comprueba si la cadena contiene solo dígitos o caracteres alfabéticos (letras) y devuelve True(verdadero) o False(falso) de acuerdo al resultado.
# Demostración del método the isalnum():
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
t = 'Six lambdas'
print(t.isalnum())

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

#  método isalpha() es más especializado, se interesa en letras solamente.
# Ejemplo 1: Demostración del método isapha():
print("Moooo".isalpha())
print('Mu40'.isalpha())

#  método isdigit() busca solo dígitos - cualquier otra cosa produce False(falso) como resultado.
print('2018'.isdigit())
print("Year2019".isdigit())

# método islower() es una variante de isalpha() - solo acepta letras minúsculas.
print("Moooo".islower())
print('moooo'.islower())

# El método isspace() identifica espacios en blanco solamente - no tiene en cuenta ningún otro carácter (el resultado es entonces False).
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# El método isupper() es la versión en mayúscula de islower() - se concentra solo en letras mayúsculas.
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# El método join() es algo complicado, así que déjanos guiarte paso a paso:

# Como su nombre lo indica, el método realiza una unión y espera un argumento del tipo lista; se debe asegurar que todos los elementos de la lista sean cadenas: de lo contrario, el método generará una excepción TypeError.
# Todos los elementos de la lista serán unidos en una sola cadena pero...
# ... la cadena desde la que se ha invocado el método será utilizada como separador, puesta entre las cadenas.
# La cadena recién creada se devuelve como resultado.

# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))
print("!".join(["omicron", "pi", "rho"]))

# lower() genera una copia de una cadena, reemplaza todas las letras mayúsculas con sus equivalentes en minúsculas, y devuelve la cadena como resultado. Nuevamente, la cadena original permanece intacta.
# Demostración del método lower():
print("SiGmA=60".lower())

# lstrip() devuelve una cadena recién creada formada a partir de la original eliminando todos los espacios en blanco iniciales.
print("[" + " tau ".lstrip() + "]")

# lstrip() hace lo mismo que su versión sin parámetros, pero elimina todos los caracteres incluidos en el argumento (una cadena)
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))

# rstrip() hacen casi lo mismo que el método lstrip, pero afecta el lado opuesto de la cadena.
# Demostración del método rstrip():
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# strip() combina los efectos causados por rstrip() y lstrip() - crea una nueva cadena que carece de todos los espacios en blanco iniciales y finales.
# Demostración del método strip():
print("[" + "   aleph   ".strip() + "]")

#  replace() con dos parámetros devuelve una copia de la cadena original en la que todas las apariciones del primer argumento han sido reemplazadas por el segundo argumento.
# Demostración del método replace():
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# con el numero reemplaza 1 y con el 2 los dos
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

#  split() divide la cadena y crea una lista de todas las subcadenas detectadas. Nota: la operación inversa se puede realizar por el método join().

# Demostración del método split():
print("phi       chi\npsi".split())

# swapcase() crea una nueva cadena intercambiando todas las letras por mayúsculas o minúsculas dentro de la cadena original: los caracteres en mayúscula se convierten en minúsculas y viceversa.
# Demostración del método swapcase():
print("Yo sé que no sé nada.".swapcase())
print()

# title() realiza una función algo similar cambia la primera letra de cada palabra a mayúsculas, convirtiendo todas las demás a minúsculas.
# Demostración del método title():
print("Yo sé que no sé nada. Part 1.".title())
print()

#  upper() hace una copia de la cadena de origen, reemplaza todas las letras minúsculas con sus equivalentes en mayúsculas
# Demostración del método upper():
print("Yo sé que no sé nada. Part 2.".upper())

#  pueden ser comparadas usando el mismo conjunto de operadores que se emplean con los números.
# ==
# !=
# >
# >=
# <
# <=
# 1. Las cadenas se pueden comparar con otras cadenas utilizando operadores de comparación generales, pero compararlas con números no da un resultado razonable, porque ninguna cadena puede ser igual a ningún otro número. Por ejemplo:

# cadena == número es siempre False (falso).
# cadena != número es siempre True (verdadero).
# cadena >= número siempre genera una excepción.

# 2. El ordenamiento de listas de cadenas se puede realizar mediante:

# Una función llamada sorted(), crea una nueva, lista ordenada.
# Un método llamado sort(), el cual ordena la lista en el momento.

# 3. Un número se puede convertir en una cadena empleando la función str().

# 4. Una cadena se puede convertir en un número (aunque no todas las cadenas) empleando ya sea la función int() o float(). La conversión falla si la cadena no contiene un número válido (se genera una excepción en dicho caso).


'alpha' == 'alpha'
'alpha' != 'Alpha'

# Comparar el primer carácter diferente en ambas cadenas (ten en cuenta los puntos de código ASCII / UNICODE en todo momento),  la cadena más larga se considera mayor.
'alpha' < 'alphabet'
# Distingue entre mayusculas(se consideran menores) y minusculas 
'beta' > 'Beta'

#  si una cadena contiene solo dígitos, todavía no es un número
print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')
# no es bueno comparar cadenas con numeros
print()
print('10' == 10)
print('10' != 10)
print('10' == 1)
print('10' != 1)
# print('10' > 10)

# Ordenar listas que contienen cadenas
# sorted().La función toma un argumento (una lista) y retorna una nueva lista, con los elementos ordenados del argumento.
# Demostración de la función sorted():
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)
print()

# El segundo método afecta a la lista misma - no se crea una nueva lista. El ordenamiento se realiza por el método denominado sort()
# Demostración del método sort():
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)

# conversión de cadena a número es simple, ya que siempre es posible. Se realiza mediante una función llamada str()
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)
# transformación inversa solo es posible cuando la cadena representa un número válido. Si no se cumple la condición, espera una excepción ValueError.

# Emplea la función int() si deseas obtener un entero, y float() si necesitas un valor punto flotante.

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)

# Ejemplos

# Cifrado César.
text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

# Cifrado César - descifrar un mensaje.
cipher = input('Ingresa tu criptograma: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

#Procesador de Números.

line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")

# Validador IBAN.

iban = input("Ingresa un IBAN, por favor: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("Has introducido caracteres no válidos.")
elif len(iban) < 15:
    print("El IBAN ingresado es demasiado corto.")
elif len(iban) > 31:
    print("El IBAN ingresado es demasiado largo.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("El IBAN ingresado es válido.")
    else:
        print("El IBAN ingresado no es válido.")
