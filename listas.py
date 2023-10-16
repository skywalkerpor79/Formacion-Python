###########################
# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

# numbers[0] = 111
# print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
# print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

# print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

# ###

# del numbers[1]  # Eliminando el segundo elemento de la lista.
# print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
# print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.
###########################

# #con el negativo empieza al reves
# numbers = [111, 7, 2, 1]
# print(numbers[-1])
# print(numbers[-2])

#####################
# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)

# ###El append inserta al final

# numbers.append(4)

# print(len(numbers))
# print(numbers)

# ### Inserta en la posicion que queremos

# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)

######################
# my_list = []  # Creando una lista vacía.

# for i in range(5):
#     my_list.append(i + 1)

# print(my_list)
####################################
# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in range(len(my_list)):
#     total += my_list[i]

# print(total)
#########################
# my_list = [10, 1, 8, 3, 5]

# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]

# print(my_list)


print("Paso 1:", Beatles)
Beatles=[]

print("Paso 2:", Beatles)
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")

# Paso 3: Emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.

print("Paso 3:", Beatles)

# paso 4
print("Paso 4:", Beatles)

# paso 5
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))
