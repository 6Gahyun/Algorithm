#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input())
b = int(input())
print(a*b)


# In[2]:


a = int(input())
b = int(input())
c = int(input())

if a == b == c == 60:
    print('Equilateral')
elif a+b+c == 180:
    if a==b or b==c or c==a:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')

