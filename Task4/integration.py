#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Task 4.6
import numpy as np
import math

# defines function that calculates the integral
def I(function, x, a, b):
  f=eval(function)
  i =(b-a)/1000*sum(f)
  return i

# gives input for the function
function=input("Enter a function: ")
a=float(input("Enter lower integration boundary: "))
b=float(input("Enter upper integration boundary: "))
x=np.random.uniform(a,b,1000)

print(I(function, x, a, b))


# In[ ]:




