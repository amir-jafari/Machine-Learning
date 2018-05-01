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
# Integers

print('Hello World!!!')
print(2 + 2)
print(2 - 2)
print(2 ** 6)
print(6 * 3)
print(10%2)
print(1/2)
print(1.0/2.0)
print('P' + 'y' + 't' + 'h' + 'o' + 'n')
print('Answer to 2 + 2:', 2 + 2)
# =============================================================
# Variable + Integers

Var = 5

print('Variable = ', Var)
print('Variable + 1 = ', Var + 1)
print('Variable x Variable = ', Var * Var)

print(type(1))
print(type(-1))
print(type(0.5))
print(type(1/2))
print(type(1.0/2.0))

# =============================================================
# Strings

First_name = 'Amir'
Sur_name = 'Jafari'

print(len(First_name))
Full_name = First_name + Sur_name
print(Full_name + '     !!!!')

Convert_int_str = str(1)

print(First_name.upper())
print(First_name.lower())
print(First_name.capitalize())
New_name = First_name.replace('Amir', 'Martin') + ' ' +Sur_name.replace('Jafari', 'Hagan')
print(New_name)

My_string = "Hello World!"

print( My_string[4])
print( My_string.split(' '))
print( My_string.split('r'))

# =============================================================
# Booleans

Number_1 = True
Number_0 = False
type(Number_1)

print(not Number_1)

# =============================================================
# Logical operators

Var  = 1
Var2 = 2

print(Var > Var2)

Var3 = Var > Var2

print(Var3)
print(Var3 +1 )
print(Var == Var2)
print(Var != Var2)

print(Var < 2 and Var >2)
# =============================================================
# Accessing Strings
My_String = 'Amir Jafari'

print(My_String[0])
print(My_String[0:1])
print(My_String[0:2])

print(My_String[::-1])

Find = My_String.find('Amir')
print(Find)
# =============================================================
# Useful Commands

str(1)
bool(1)
int(False)
float(False)
float(1)
str(1/2)
int(1.2)
str(True)
str(None)
