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
# If statement

a = True
if a == 1:
    print('True')
else:
    print('False')

# -------------------------------------------------
Grade = 95

if Grade >= 92:
    print("You got an A")
elif Grade > 87 and Grade <92:
    print('You got an A-')
elif Grade < 87:
    print("You need to redo the course")
else:
    print("Something is Wrong !!!")