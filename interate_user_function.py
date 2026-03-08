#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Task 4.19
import numpy as np
from numpy import sin, cos, exp, pi
import scipy.integrate as integrate

print("User Input")

# input for a function and variable
function = input("Enter a function with variable x: ")
variable = input("Enter a value for x: ")

# detects and handles errors in the input
try:
    x = float(variable) 
    result = eval(function)
    print(f"f({x}) = {result}")

except NameError as e:
    print("\nNameError: The program cannot recognize the input")
    print(f"Details: {e}")

except SyntaxError as e:
    print("\nSyntaxError: There is a Syntax error")
    print(f"Details: {e}")

except Exception as e:
    print(f"\nThere is an unexcpected error: {e}")

# creates a function for the scipy integral
def function1(x_values):
    x = x_values  
    return eval(formula)

# evaluates the integral using integrate.quad
integral= integrate.quad(function1, 0, pi)
print(f"SciPy Result: {quad_result:}")

# generates data for the x values
N=1000000
x = np.random.uniform(0, pi, N)

# evaluates the formula
y_values = eval(target_formula)

# uses monte carla integration to evaluate the integral
width = (pi - 0)
average_height = np.mean(y_values)
mc_result = width * average_height

print(f"Monte Carlo Result: {mc_result:}")


# In[ ]:




