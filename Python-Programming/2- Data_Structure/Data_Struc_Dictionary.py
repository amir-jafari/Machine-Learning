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
# Dictionary

empty_dict = {}
my_dict = {'a': 1, 'b': 2, 'c': "Amir"}
print(my_dict['a'])
del my_dict['b']

print(my_dict.get('e'))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print('c' in my_dict)
# ----------------------------------------
# set
my_list = [1, 2, 3, 4]
var_set = set(my_list)
var_list = list(var_set)
print(type(var_set))
print(type(var_list))

# ----------------------------------------
# Zip
a = ['a', 'b', 'c', 'd', 'e']
b = [1, 2, 3, 4, 5]
Dic = dict(zip(a, b))

print(Dic)
del Dic['a']
print(Dic)

