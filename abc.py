#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
# Defining the variables
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))

# Defining d as a variable
d=b**2-4*a*c


# Defining the conditions and output
if d>0:
    
 x1=(-b+math.sqrt(d))/(2*a)
 x2=(-b-math.sqrt(d))/(2*a)

 print("x1:", x1)
 print("x2:", x2)

elif d==0:
 x= -b/(2*a)
 print(x)

else:
 print("no real solution")


