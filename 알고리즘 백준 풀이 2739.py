#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = int(input('정수 A : '))
b = int(input('정수 B : '))
print(a + b)


# In[5]:


a, b = map(int, input().split())
print(a)
print(a+b)


# In[7]:


y = int(input('y : '))
print(y-543)


# In[6]:


a = int(input())
for i in range(1,10):
    print('%s * %d = %a' %(a, i, a*i))

