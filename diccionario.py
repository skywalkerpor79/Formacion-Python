
# # dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
# # phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
# # empty_dictionary = {}
# # print(dictionary['gato'])
# # print(phone_numbers['Suzy'])



# dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
# words = ['gato', 'león', 'caballo']

# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "no está en el diccionario")



# dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
# dictionary['cisne'] = 'cygne'
# print(dictionary)

# dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
# dictionary.update({"pato": "canard"})
# print(dictionary)

# dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
# del dictionary['perro']
# print(dictionary)

# #popitem elimina el ultimo elemento de la lista
# dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
# dictionary.popitem()
# print(dictionary)    



# 1. Los diccionarios son *colecciones indexadas de datos, mutables y desordenadas. (*En Python 3.6x los diccionarios están ordenados de manera predeterminada.

# Cada diccionario es un par de clave : valor. Se puede crear empleado la siguiente sintaxis:

# my_dictionary = {
#     key1: value1,
#     key2: value2,
#     key3: value3,
#     }


# 2. Si se desea acceder a un elemento del diccionario, se puede hacer haciendo referencia a su clave colocándola dentro de corchetes (Ejemplo 1) o utilizando el método get() (Ejemplo 2):

# pol_esp_dictionary = {
#     "kwiat": "flor",
#     "woda": "agua",
#     "gleba": "tierra"
#     }

# item_1 = pol_esp_dictionary["gleba"]    # Ejemplo 1.
# print(item_1)    # salida: tierra

# item_2 = pol_esp_dictionary.get("woda")    # Ejemplo 2.
# print(item_2)    # salida: agua


# 3. Si se desea cambiar el valor asociado a una clave específica, se puede hacer haciendo referencia a la clave del elemento, a continuación se muestra un ejemplo:

# pol_esp_dictionary = {
#     "zamek" : "castillo",
#     "woda"  : "agua",
#     "gleba" : "tierra"
#     }

# pol_esp_dictionary["zamek"] = "cerradura"
# item = pol_esp_dictionary["zamek"]    
# print(item)  # salida: cerradura


# 4. Para agregar o eliminar una clave (junto con su valor asociado), emplea la siguiente sintaxis:

# phonebook = {}    # un diccionario vacío

# phonebook["Adán"] = 3456783958    # crear/agregar un par clave-valor
# print(phonebook)    # salida: {'Adán': 3456783958}

# del phonebook["Adán"]
# print(phonebook)    # salida: {}


# Además, se puede insertar un elemento a un diccionario utilizando el método update(), y eliminar el ultimo elemento con el método popitem(), por ejemplo:

# pol_esp_dictionary = {"kwiat": "flor"}

# pol_esp_dictionary.update({"gleba": "tierra"})
# print(pol_esp_dictionary)    # salida: {'kwiat': 'flor', 'gleba': 'tierra'}

# pol_esp_dictionary.popitem()
# print(pol_esp_dictionary)    # salida: {'kwiat': 'flor'}


# 5. Se puede emplear el bucle for para iterar a través del diccionario, por ejemplo:

# pol_esp_dictionary = {
#     "zamek": "castillo",
#     "woda": "agua",
#     "gleba": "tierra"
#     }

# for item in pol_esp_dictionary:
#     print(item) 

# # salida: zamek
# #         woda
# #         gleba





# 6. Si deseas examinar los elementos (claves y valores) del diccionario, puedes emplear el método items(), por ejemplo:

# pol_esp_dictionary = {
#     "zamek" : "castillo",
#     "woda"  : "agua",
#     "gleba" : "tierra"
#     }

# for key, value in pol_esp_dictionary.items():
#     print("Pol/Esp ->", key, ":", value)


# 7. Para comprobar si una clave existe en un diccionario, se puede emplear la palabra clave reservada in:

# pol_esp_dictionary = {
#     "zamek" : "castillo",
#     "woda"  : "agua",
#     "gleba" : "tierra"
#     }

# if "zamek" in pol_esp_dictionary:
#     print("Si")
# else:
#     print("No")


# 8. Se puede emplear la palabra reservada del para eliminar un elemento, o un diccionario entero. Para eliminar todos los elementos de un diccionario se debe emplear el método clear():

# pol_esp_dictionary = {
#     "zamek" : "castillo",
#     "woda"  : "agua",
#     "gleba" : "tierra"
#     }

# print(len(pol_esp_dictionary))    # salida: 3
# del pol_esp_dictionary["zamek"]    # eliminar un elemento
# print(len(pol_esp_dictionary))    # salida: 2

# pol_esp_dictionary.clear()   # eliminar todos los elementos
# print(len(pol_esp_dictionary))    # salida: 0

# del pol_esp_dictionary    # elimina el diccionario


# 9. Para copiar un diccionario, emplea el método copy():

# pol_esp_dictionary = {
#     "zamek" : "castillo",
#     "woda"  : "agua",
#     "gleba" : "tierra"
#     }

# copy_dictionary = pol_esp_dictionary.copy()



# school_class = {}

# while True:
#     name = input("Ingresa el nombre del estudiante: ")
#     if name == '':
#         break
    
#     score = int(input("Ingresa la calificación del estudiante (0-10): "))
#     if score not in range(0, 11):
# 	    break

#     if name in school_class:
#        school_class[name] += (score,)
#     else:
#        school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)


d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list)
print(t)

colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)