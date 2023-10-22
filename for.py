import time

# for i in range(10):
#     print("El valor de i es actualmente", i)
# for i in range(2, 8):
#     print("El valor de i es actualmente", i)
# #el tercer parámetro del for es un incremento
# for i in range(2, 8, 3):
#     print("El valor de i es actualmente", i)
    
# for i in range(5):
#     print("Missisipi")
#     time.sleep(1)

# break - ejemplo

# print("La instrucción break:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")


# # continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

# largest_number = -99999999
# counter = 0


# for i in range(5):
#     print(i)
# else:
#     print("else:", i)
# var=1
# while var<10:
#     print("#")
#     var=var<<1
    
# my_list=[1,2,3,4]
# print(my_list[-3:-2])

nums=[1,2,3]
vals=nums
del vals[1:2]
print(nums)
print(vals)

z=10
y=0
x=y<z and z>y or y> z and z<y
print(x)

my_list=[1,2,3]
for v in range(len(my_list)):
    my_list.insert(1,my_list[v])
print(my_list)

vals=[0,1,2]
vals.insert(0,1)
del vals[1]
print (vals)

for i in range(1):
    print("#")
else:
    print("#")

a=1
b=0
c=a&b
d=a|b
e=a^b
print(c+d+e)

nums=[1,2,3]
vals=nums[-1:-2]
print(nums)
print(vals)

var=0
while var<6:
    var +=1
    if var % 2 ==0:
        continue
    print("#")

x=1
x=x==x
print(x)

i=0
while i<=3:
    i+=2
    print("*")