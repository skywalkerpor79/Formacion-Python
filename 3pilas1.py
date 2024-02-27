# Puntos Clave

# 1. Una pila es un objeto diseñado para almacenar datos utilizando el modelo LIFO. La pila normalmente realiza al menos dos operaciones, llamadas push() y pop().


# 2. La implementación de la pila en un modelo procedimental plantea varios problemas que pueden resolverse con las técnicas ofrecidas por la POO (Programación Orientada a Objetos).


# 3. Un método de clase es en realidad una función declarada dentro de la clase y capaz de acceder a todos los componentes de la clase.


# 4. La parte de la clase en Python responsable de crear nuevos objetos se llama constructor y se implementa como un método de nombre __init__.


# 5. Cada declaración de método de clase debe contener al menos un parámetro (siempre el primero) generalmente denominado self, y es utilizado por los objetos para identificarse a sí mismos.


# 6. Si queremos ocultar alguno de los componentes de una clase del mundo exterior, debemos comenzar su nombre con __. Estos componentes se denominan privados.



###Pila en forma procidemental
# stack = []

# def push(val):
#     stack.append(val)

# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val

# push(3)
# push(2)
# push(1)

# print(pop())
# print(pop())
# print(pop())

# ### Pila orienta a objetos
# class Stack:  # Definiendo la clase de la pila.
#     def __init__(self):  # Definiendo la función del constructor.
#         #self.stack_list=[] si lo llamaos asin seria publica
#         self.__stack_list = []
#         # si ponemos los dos guiones al principio se vuelve privado y solo se puede acceder desde la classe con eso creariamos la encapsulacion
#     def push(self,val):
#         self.__stack_list.append(val)
    
#     def pop(self):
#         val=self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val

    
        
# stack_object_1 = Stack()  # Instanciando el objeto.
# #print(len(stack_object.stack_list))

# #### ejemplo con una pila
# # stack_object.push(3)
# # stack_object.push(2)
# # stack_object.push(1)

# # print(stack_object.pop())
# # print(stack_object.pop())
# # print(stack_object.pop())

# # ejemplo con 2 pilas 
# stack_object_2=Stack()
# stack_object_1.push(3)
# stack_object_2.push(stack_object_1.pop())

# print(stack_object_2.pop())

# ### ejemplo 2
# class Stack:
#     def __init__(self):
#         self.__stack_list = []

#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val


# little_stack = Stack()
# another_stack = Stack()
# funny_stack = Stack()

# little_stack.push(1)
# another_stack.push(little_stack.pop() + 1)
# funny_stack.push(another_stack.pop() - 2)

# print(funny_stack.pop())

#ejemplo 3 añadimos una sublclase
# class Stack:
#     def __init__(self):
#         self.__stack_list = []

#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val


# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0

# #Ejemplo 4
# class Stack:
#     def __init__(self):
#         self.__stackList = []

#     def push(self, val):
#         self.__stackList.append(val)

#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val


# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())
