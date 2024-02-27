# class ThesimplestClass:
#     pass

# my_first_objet= ThesimplestClass()

#############
#  Una variable de instancia es una propiedad cuya existencia depende de la creación de un objeto. Cada objeto puede tener un conjunto diferente de variables de instancia.

# Además, se pueden agregar y quitar libremente de los objetos durante su vida útil. Todas las variables de instancia de objeto se almacenan dentro de un diccionario dedicado llamado __dict__, contenido en cada objeto por separado.

# 2. Una variable de instancia puede ser privada cuando su nombre comienza con __, pero no olvides que dicha propiedad aún es accesible desde fuera de la clase usando un nombre modificado construido como < codel>_ClassName__PrivatePropertyName.

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

print(example_object_1.__dict__)
#############

# 3. Una variable de clase es una propiedad que existe exactamente en una copia y no necesita ningún objeto creado para ser accesible. Estas variables no se muestran como contenido de __dict__.

# Todas las variables de clase de una clase se almacenan dentro de un diccionario dedicado llamado __dict__, contenido en cada clase por separado.


# 4. Una función llamada hasattr() se puede utilizar para determinar si algún objeto o clase contiene cierta propiedad especificada.