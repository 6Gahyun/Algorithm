#!/usr/bin/env python
# coding: utf-8

# In[1]:


#### 2439 별 찍기 -2
N = int(input())
a = ' '
b = '*'
for i in range(1, N+1):
    print(f'{a*(N-i)}{b*i}')


# In[ ]:


#### 10951 A+B -4
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break

