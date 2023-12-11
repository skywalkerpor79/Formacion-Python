# def happy_new_year(wishes = True):
#     print("Tres...")
#     print("Dos...")
#     print("Uno...")
#     if not wishes:
#         return
    
#     print("¡Feliz año nuevo!")

# happy_new_year()
# happy_new_year(False)

# def boring_function():
#     return 123

# x = boring_function()

# print("La función boring_function ha devuelto su resultado. Es:", x)
#############
#Seria com un null
# value = None
# if value is None:
#     print("Lo siento, no contienes ningún valor")

# def strange_function(n):
#     if(n % 2 == 0):
#         return True
# print(strange_function(2))
# print(strange_function(1))
###########
# def list_sum(lst):
#     s = 0
    
#     for elem in lst:
#         s += elem
    
#     return s
# print(list_sum([5, 4, 3]))
############
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))


def fun(soc=2,out=3):
    return soc * out

print(fun(3))

tup=(1,)+(1,)
tup=tup+tup
print(len(tup))

