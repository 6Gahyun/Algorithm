#!/usr/bin/env python
# coding: utf-8

# ##### #1834 나머지와 몫이 같은 수

# In[11]:


N = int(input())
a=0
for i in range(1, N):
        a += N*i+i
print(a)

