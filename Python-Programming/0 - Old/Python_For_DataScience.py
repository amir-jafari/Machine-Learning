x = 5
print( x)
y = x + 2
print( y)
y = x - 2
print( y)
y = x * 2
print( y)
y = x ** 2
print( y)
y = x % 2
print( y)
y = x / float(2)
print( y)
# ----------------------------------------
my_string = 'thisStringIsAwsome'
print( my_string)
print( my_string * 2)
print( my_string + 'Innit')
d = 'm' in my_string
print( d)
# ----------------------------------------
a = 'is'
b = 'nice'
my_list = ['my', 'list', a, b]
my_list2 = [[4, 5, 6, 7], [3, 4, 5, 6]]
print( my_list)
print( my_list2)
print( my_list[1:3])
print( my_list[1:])
print( my_list[:3])
print( my_list[:])

print( my_list2[1][0])
print( my_list2[1][:2])

print( my_list. index(a))
print( my_list. count(a))
print( my_list. append('!'))
print( my_list)
print( my_list. remove('!'))
print( my_list)
del my_list[0:1]
print( my_list)
print( my_list. extend('!'))
print( my_list)
print( my_list. pop(-1))
print( my_list. insert(0, '!'))
print( my_list)

# ----------------------------------------
print( my_string[3])
print( my_string[4:9])

print( my_string.upper())
print( my_string.lower())
print( my_string.count('w'))
print( my_string.replace('e', 'i'))
print( my_string.strip())

# ----------------------------------------
import numpy
import numpy as np
from math import pi

my_list = [1, 2, 3, 4]
my_array = np.array(my_list)
print( my_array)
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print( my_2darray)

print( my_array[1])
print( my_array[0:2])

print( my_2darray[:, 0])

print( my_array > 3)
print( my_array * 2)

print( my_array + np.array([5, 6, 7, 8]))

print( my_array.shape)
print( my_2darray.shape)