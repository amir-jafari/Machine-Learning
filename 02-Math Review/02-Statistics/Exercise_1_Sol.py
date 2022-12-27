from random import uniform

select1 = {}
select2 = {}
select3 = {}
select4 = {}

def generate_random_number(x,y):
    for i in range(0, 10000):
        f_rand = uniform(0, 1)
        if f_rand < y[0]:
            select1[i] = x[0]
        if f_rand < y[1]:
            select2[i] = x[1]
        if f_rand < y[2]:
            select3[i] = x[2]
        if f_rand < y[3]:
            select4[i] = x[3]


    print (len(select1))
    print (len(select2))
    print (len(select3))
    print (len(select4))

x =[1, 2, 3, 4]
y =[0.1, 0.2, 0.3, 0.4]

generate_random_number(x, y)