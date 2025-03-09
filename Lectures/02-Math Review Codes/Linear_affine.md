# Understanding Why $y = 2x + 1$ is Affine but Not Linear

## **Mathematical Explanation**
A function is **linear** if it satisfies both:

1. **Additivity**: 
$f(x_{1} + x_2) = f(x_1) + f(x_2)$
2. **Homogeneity** (or scalar multiplication): 
$f(\lambda x) = \lambda f(x) $ for any scalar $ \lambda$.

### **Step 1: Checking Additivity**


$f(x_1 + x_2) = 2(x_1 + x_2) + 1 = 2x_1 + 2x_2 + 1$


On the other hand,


$(x_1) + f(x_2) = (2x_1 + 1) + (2x_2 + 1) = 2x_1 + 2x_2 + 2$


Since $( f(x_1 + x_2) \neq f(x_1) + f(x_2) )$ (there is an extra \( +1 \) term), additivity does not hold.

### **Step 2: Checking Homogeneity**
For a scalar $( \lambda )$:


$f(\lambda x) = 2(\lambda x) + 1 = 2\lambda x + 1$


On the other hand,


$\lambda f(x) = \lambda (2x + 1) = 2\lambda x + \lambda$


Since $f(\lambda x) \neq \lambda f(x)$ (there is an extra $+1$ term), homogeneity does not hold.

Since neither condition is satisfied, $f(x) = 2x + 1$ is **not a linear function**.

---

## **Affine Functions**
A function is **affine** if it is of the form:

$f(x) = Ax + b$

where $(A)$ is a linear transformation (matrix or scalar) and $(b)$ is a constant vector (or scalar).
In our case, 

$f(x) = 2x + 1$

which fits the affine form where $A = 2$ and $b = 1$. Therefore, $y = 2x + 1$ is **affine but not linear**.

---

## **Key Takeaway**
- A **linear function** must pass through the origin and satisfy additivity and homogeneity.
- An **affine function** is a shifted linear function, meaning it is linear plus a constant term.
- Since $y = 2x + 1$ has a constant term $+1$ , it **does not satisfy linearity but is affine**.

