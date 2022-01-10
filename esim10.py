from sympy import Symbol, Derivative,solve
import numpy as np
import matplotlib.pyplot as pyplot

x= Symbol('x')

function= x**3 - 9*x + 5

fprime = function.diff(x)
turningPoint=solve(fprime,x)
print("The turning points of the function are x = "+str(turningPoint))