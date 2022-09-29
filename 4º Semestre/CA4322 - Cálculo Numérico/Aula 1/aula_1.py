import numpy as np
import matplotlib.pyplot as plt
from sympy import *

"""
#Exemplo 1

x = np.linspace(-10, 10, 20)
y = np.sin(x) + 2*x +1
plt.plot(x,y,x,x)
plt.show()

# Exemplo 2 - Limite

x = symbols('x')
f = (x-2)/(x**2 - 4)
r = limit(f,x,2)
print("Limite =", r)

# Exemplo 3 - Derivada

x = symbols('x')
eq = (cos(x)+ x**2)**2
r = diff(eq,x)
print("Derivada = ",r)

# Exemplo 4 - Integral

x,y = symbols('x y')
y = x**2*exp(x)
print("Integral =",integrate(y, x))

"""