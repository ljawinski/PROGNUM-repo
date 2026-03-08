#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Task 4.17
import math
from scipy.constants import pi
import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate


# defines the gaussian function
def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

# input for the different variables
A=float(input("value for A"))
x0=float(input("value for x0"))
sigma=float(input("value for sigma"))
z0=float(input("value for z0"))

# input for the integration limits
a=float(input("lower integration limit"))
b=float(input("upper integration limit"))

# calculates the integral
a_total=integrate.quad(lambda x:gauss(x, 1, 0, 2, 0), a, b)
print("Area under the curve: ", a_total[0])

# plots the function
x=np.linspace(-10, 10, 200)
f=gauss(x, A, x0, sigma, z0)

plt.plot(x,f, label=f"Area under the curve: {a_total[0]}")

# marks the area of the integral
mask= (x>=a)&(x<=b)
plt.fill_between(x[mask], f[mask])

# adds a legend
plt.legend()
plt.show()





