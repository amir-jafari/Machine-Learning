# %%%%%%%%%%%%% Python %%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Martin Hagan----->Email: mhagan@okstate.edu
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# %%%%%%%%%%%%% Date:
# V1 Jan - 01 - 2017
# V2 Sep - 29 - 2017
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Base Python %%%%%%%%%%%%%%%%%%%%%%%%%%%%
# =============================================================
# List

My_list = [1, 2, 'p', 3, 'y']

print( My_list[0])
print( My_list[1:3])
print( My_list[2:])
print( My_list[:2])
print( My_list[2:-1])
print( len(My_list))

print( My_list. append(37))
print( My_list)
print( My_list. pop())
print( My_list)
print( My_list. pop(1))
print( My_list)
print( My_list. insert(2, 'z'))
print( My_list)
print( My_list. remove('p'))
print( My_list)


del My_list[0]
print( My_list)

My_list1 = My_list + [0]
print( My_list)
a =9 in My_list
print(a)
# ------------------------------------------------------------------
words = ["this", "is", "a", "list", "of", "words"]

print(' '.join(words))
print('Cool'.join(words))
print(''.join(words))
this_string = "there"
print("Hello %s!" % this_string)
# ------------------------------------------------------------------
numbers = [10, 20, 30, 40]
max(numbers)
min(numbers)


List_Names = ['Amir', 'Jafari', 'Martin']
max(List_Names)
min(List_Names)

len(List_Names)
List_Names.append('Hagan')
print(List_Names)
len(List_Names)

Update_list = List_Names.pop()
print(Update_list)
print(List_Names)
len(Update_list)
index = List_Names.index('Amir')

# =============================================================
# List Comprehension

x = [x*5 for x in range(5)]
print( x)
x = [x for x in range(5) if x % 2 == 0]
print( x)