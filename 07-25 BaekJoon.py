#!/usr/bin/env python
# coding: utf-8

# In[5]:


X = int(input())
N = int(input())
price = []
for i in range(N):
    a, b = map(int, input().split())
    c = a*b
    price.append(c)
if X == sum(price):
    print('Yes')
else:
    print('No')


# In[11]:


Y = int(input())
if Y%4==0:
    if Y%100!=0 or Y%400==0:
        print(1)
    else:
        print(0)
else:
    print(0)

