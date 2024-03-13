# %%%%%%%%%%%%% Python %%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Martin Hagan----->Email: mhagan@okstate.edu
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# %%%%%%%%%%%%% Date:
# V1 Jan - 04 - 2018
# V2 May - 12 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Math Python %%%%%%%%%%%%%%%%%%%%%%%%%%%%
# =============================================================
# ------------------------------------------------------------
# -------------Linear Algebra --------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# -------------Symbolic  -------------------------------------
# ------------------------------------------------------------

from sympy import *
x = symbols('x')
y = symbols('y')

f1 = (x+y)**2
print(f1)

f2 = expand(( x + y) ** 3)
print(f2)

f3 = simplify((x + x * y) / x)
print(f3)


l1 = limit(x, x, oo)
print(l1)

l2 = limit(1/x, x, oo)
print(l2)

l3 = limit(x**x, x, 0)
print(l3)

l4 =limit((tan(x+y)-tan(x))/y, y, 0)
print(l4)


d1 = diff(sin(x), x)
print(d1)

d2 = diff(sin(2*x), x)
print(d2)



s1 = series(cos(x), x)
print(s1)

s2 = series(1/cos(x), x)
print(s2)

i1 = integrate(6*x**5, x)
print(i1)

i2 = integrate(sin(x), x)
print(i2)

i3 = integrate(2*x + sinh(x), x)
print(i3)

i4 = integrate(x**3, (x, -1, 1))
print(i4)

i5= integrate(sin(x), (x, 0, pi/2))
print(i5)


i6 = integrate(cos(x), (x, -pi/2, pi/2))
print(i6)

e1 = solve(x**4 - 1, x)
print(e1)

e2 = solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y])
print(e2)

f = x**4 - 3*x**2 + 1
factor(f)



from sympy import Matrix

M1 = Matrix([[1,0], [0,1]])
print(M1)

M2 = Matrix([[1,x], [y,1]])
print(M2)
