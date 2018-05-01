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
# For loops

List_names = ['Amir', 'Jafari', 'Martin', 'Hagan' ]
for name in List_names:
    print('Your name is :  ' + name)

# ----------------------------------------------
for i in range(5):
    print(i)
# ----------------------------------------------
for i in range(0, 6, 2):
    print(i)
# ----------------------------------------------

times_2 = []
for i in range(5):
    times_2.append(i*2)
    print(times_2)
# ----------------------------------------------
S = 0
while S < 10:
    print('S = '+str(S))
    S += 1


# =============================================================
# List Comprehension

x = [x*5 for x in range(5)]
print( x)
x = [x for x in range(5) if x % 2 == 0]
print( x)

# =============================================================
# Generic loops
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

d2 = [i for i,v in enumerate(nums) if v >= 5]
print(d2)


d3 = [v for i,v in enumerate(nums) if v >= 5]
print(d3)