#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Task 2.10
Year = int(input("Enter Year"))
Month = int(input("Enter Month"))
Day = int(input("Enter Day"))
Y=int(Year)
M=int(Month)
D=int(Day)
J=367*Y-7*(Y+(M+9)/12)/4-3*((Y*(M-9/7)/100)+1)/4+(275*M)/9+D+1721029-0.5
print(J)


# In[ ]:




