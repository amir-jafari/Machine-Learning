import numpy as np
c = [1, 2, 3, 4, 5, 6, 7]
d = sum(c)
# -------------------------------------------------------
f = []
for i in range(10):
    if i == 0:
        f = [0]
    else:
        f.append((1.0/i)+f[i-1])

print( f)
# -------------------------------------------------------
a = ['car', 'dog', 'bite', 'dab', 'rac', 'god']
b = ['rac', 'dog', 'bad', 'dad']

for i in range(len(a)):
    word = sorted(a[i])
    for dummy in a:
        if word == sorted(dummy) and dummy != a[i]:
            print( "%s is anagram" % dummy)
# -------------------------------------------------------

e = [1, 2, 4, 5, 7, 3, 5, 6, 5]
x = []
for i in range(len(e)):
    v1 = e[i]
    for index, val in enumerate(e):
        if val + v1 == 10:
            x. append([index, i])
print( x)

# -------------------------------------------------------
e1 = [[1, 2], [2, 5], [4, 3], [5, 2], [7, 2], [3, 1], [5, 1], [2, 5], [2, 1]]
x = []
for i in range(len(e1)):
    a = list(reversed(e1[i]))
    for index, val in enumerate(e1):
        if val == a:
            x.append([index, i])
print( x)
x = np.array(x)
x1 = np.zeros(shape=(len(x), 2))
for index in range(len(x)):
    if not np.any(x[1] - np.flipud(x[index])):
        x1 = np.delete(x, index, 0)

print( x1)
# -------------------------------------------------------
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print( "list1 = %s" % list1)
print( "list2 = %s" % list2)
print( "list3 = %s" % list3)

# -------------------------------------------------------
def multipliers():
    return [lambda x: i * x for i in range(4)]


print( [m(2) for m in multipliers()])
# -------------------------------------------------------

class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print( Parent.x, Child1.x, Child2.x)
Child1.x = 2
print( Parent.x, Child1.x, Child2.x)
Parent.x = 3
print( Parent.x, Child1.x, Child2.x)

# -------------------------------------------------------
def div1(x, y):
    print( "%s/%s = %s" % (x, y, x / y))


def div2(x, y):
    print( "%s//%s = %s" % (x, y, x // y))


div1(5, 2)
div1(5., 2)
div2(5, 2)
div2(5., 2.)
# -------------------------------------------------------
list = [ [ ] ] * 5
print( list)  # output?
list[0].append(10)
print( list ) # output?
list[1].append(20)
print( list ) # output?
list.append(30)
print( list ) # output?
# -------------------------------------------------------

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

c = factorial(5)
print( c)
# -------------------------------------------------------
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

d = fib(12)
print( d)
# -------------------------------------------------------
def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

di = fibi(12)

print( di)
# -------------------------------------------------------

f = ['aaa', 'bbb', 'ccc', 'aaa', 'bbb', 'aaa']


f_sort = sorted(f)
l1 = len(f_sort)
s1 =[]
for index, d1 in enumerate(f_sort):
    print( index)
    if index == l1-1:
        break
    elif f_sort[index] == f_sort[index+1]:
        s1.append(index)
print( s1)
# -------------------------------------------------------
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]

a_dot_b = np.dot(a, b)
print( a_dot_b)
# -------------------------------------------------------
import math

def compute_surface_area_cylindar(radius, height):
    surface_area = 2 * math.pi * radius * height + 2 * math.pi * math.pow(radius, 2)
    return surface_area


#radius = int(input("Radius of circle:"))
#height = int(input("Height of the cylinder:"))

radius = 2
height = 2
print((compute_surface_area_cylindar(radius,height)))
# -------------------------------------------------------

c =[20, 3, 4, 5, 6]

print( 55 in c)
print( c.index(5))


def square(x):
    return (x**2)
def cube(x):
    return (x**3)

funcs = [square, cube]
for r in range(5):
    value = map(lambda x: x(r), funcs)
    print( value)
# -------------------------------------------------------

a =['ana', 'dad', 'Amir']

def is_palndromie(a):
    x = [x for x in a]
    
    if x == x[::-1]:
        return True
    else:
        return False

answer = is_palndromie(a[2])
print( answer)

# -------------------------------------------------------

a = ['ana', 'dad', 'Amir']


def is_palndromie(a):
    x = [x for x in a]

    if x == x[::-1]:
        print('%s is is palndromie' % a)
    else:
        print('%s is is not palndromie' % a)

for i in range(len(a)):
    answer = is_palndromie(a[i])

# -------------------------------------------------------
a1 = a[0]
x =[x for x in a1]
if x == x[::-1]:
    print('%s is is palndromie' %a1)
else:
    print('%s is is not palndromie' %a1)