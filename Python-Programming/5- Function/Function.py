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
# Functions

First_name = 'Amir'
Sur_name = 'Jafari'

def full_name(a, b):
    return a + ' ' + b

Full = full_name(First_name,Sur_name)
print(Full)

# ---------------------------------------------------------------

Grade = 95
def Class_Grades(Grade):
    if Grade >= 92:
        print("You got an A")
    elif Grade > 87 and Grade <92:
        print('You got an A-')
    elif Grade < 87:
        print("You need to redo the course")
    else:
        print("Something is Wrong !!!")

Grade = 95
print(Class_Grades(Grade))