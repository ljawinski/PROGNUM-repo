#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Task 4.3
import numpy as np

# user input
user= input("R, S or P: ")

# generates random variable
variables=np.array(['R', 'S', 'P'])
output=np.random.randint(0, len(variables), 1)
a=variables[output]
print("computer response: ", a)

# determines outcome of the game
if user=='R' and a=='S':
    print("You win!")
    
if user=='R' and a=='P':
    print("You lose")
    
if user=='S' and a=='R':
    print("You lose")
    
if user =='S' and a=='P':
    print("You win!")
    
if user=='P' and a=='R':
    print("You win!")
    
if user=='P' and a=='S':
    print("You lose")
    
if user==a:
    print("No winner")

