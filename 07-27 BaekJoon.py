#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = int(input())
b = input() 
b_list = list(map(int, b))
print(a * b_list[2])
print(a * b_list[1])
print(a * b_list[0])
print(a * int(b))

