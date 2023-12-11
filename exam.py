def fun(x,y,z):
    return x+2*y+3*z
print(fun(0,z=1,y=3))
    
def func_1(a):
    return a**a
def func_2(a):
    return func_1(a)*func_1(a)
print (func_2(2))

# my_list = ['Mary','had', 'a','little','lamb']
# def my_list(my_list):
#     del my_list[3]
#     my_list[3]='ram'
# print(my_list(my_list))

def fun(x):
    global y
    y=x*x
    return y
fun (2)
print(y)

# try:
#     value=input("Ingresa un valor: ")
#     print(value/value)
# except ValueError:
#     print("Entrada incorrecta...")
# except ZeroDivisionError:
#     print("Entrada errónea...")
# except TypeError:
#     print("Entrada muy erronea...")
# except:
#     print("!Buuu")

dictionary={}
my_list=['a','b','c','d']
for i in range(len(my_list)-1):
    dictionary[my_list[i]]= (my_list[i],)

for i in sorted(dictionary.keys()):
    k=dictionary[i]
    print(k[0])                 


# def func(a,b):
#     return a**a
# print(func(2))

def any():
    print(var+1,end='')

var=1
any()
print(var)


tup=(1,2,4,8)
tup=tup[1:-1]
tup=tup[0]
print(tup)

dictionary={'one': 'two', 'three':'one', 'two':'three'}
v=dictionary['one']
for k in range(len(dictionary)):
    v=dictionary[v]
print(v)

def fun(x):
    x+=1
    return x
x=2
x=fun(x+1)
print(x)

def f(x):
    if x==0:
        return 0
    return x + f(x-1)
print (f(3))

# def fun(x):
#     if x % 2==0:
#         return 1
#     else:
#         return
# print (fun(fun(2))+1)

def fun (inp=2, out=3):
    return inp *out
print (fun(out=2))

my_list= [x*x for x in range(5)]
def fun(lst):
    del lst[lst[2]]
    return lst
print(fun(my_list))

z=0
y=10
x=y<z and z> y or y > z and z<y
print (x)

# try:
#     print(5/0)
#     break
# except:
#     print("Lo siento, algo salió mal...")
# except (ValueError, ZeroDivisionError):
# print("mala suerte...")

nums=[1,2,3]
vals =nums
del vals[:]
print(len (nums))
print(len(vals))


x=1
y=2
x,y,z=x,x,y
z,y,z=x,y,z
print(x,y,z)

# y=input()
# x=input()
# print(x+y)


def fun(x,y):
    if x==y:
        return x
    else:
        return fun(x,y-1)
print (fun(0,3))

# i=0
# while i<i+2:
#     i+=1
#     print("*")
# else:
#     print("*")

print(1//2)

# try:
#     value=input("Ingresa un valor: ")
#     print(int(value)/len(value))
# except ValueError:
#     print("Entrada incorrecta...")
# except ZeroDivisionError:
#     print("Entrada errónea...")
# except TypeError:
#     print("Entrada muy erronea...")
# except:
#     print("!buuuu")

# lst=[i for i in range(-1,-2)]
# print (lst)

# print("a","b","c",sep="sep")

# def function_1(a):
#     return None

# def function_2(a):
#     return function_1(a)*function_1(a)

# print(function_2(2))

tup= (1,2,4,8)
tup=tup[-2:-1]
tup=tup[-1]
print(tup)

# def fun(inp=2,out=3):
#     return inp*out
# print(fun(out=2))

# dct={}
# dct['1']=(1,2)
# dct['2']=(2,1)
# for x in dct.keys():
#     print(dct[x],[1], end="")

dct={'one':'two', 'three':'one', 'two':'three'}
v=dct['three']
for k in range(len(dct)):
    v=dct[v]
print(v)

a=1
b=0
a=a^b
b=a^b
a=a^b
print(a,b)


# dd={"1":"0", "0":"1"}
# for x in dd.vals():
#     print(x, end="")

# x=float(input())
# y=float(input())
# print(y ** (1/x))


# x=int(input())
# y=int(input())
# x=x%y
# x=x%y
# y=y%x
# print(y)

def fun(x):
    if x%2==0:
        return 1
    else:
        return 2
print(fun(fun(2)))

my_list=[1,2]
for v in range(2):
    my_list.insert(-1, my_list[v])
print (my_list)

num=[1,2,3]
vals =num
print (num)
print (vals)

# def func(a,b):
#     return b**a
# print(func(b=2,2))

# foo= (1,2,3)
# foo.index(0)

lst=[[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c]%2!=0:
            print("#")

x=1//5 +1/5
print(x)
