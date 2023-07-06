#!/usr/bin/env python
# coding: utf-8

# In[10]:


# 2752 정렬
import numpy as np
a = list(map(int, input().split()))
a.sort()
print(a[0], a[1], a[2])


# In[2]:


# 1264 모음의 개수
lst = ['A', 'E', 'I', 'O', 'U']
while True:
    num=0
    s = input().upper()
    if s == "#":
        break
    for i in s:
        if i in lst:
            num+=1
    print(num)


# In[4]:


# 5524 입실관리
N = int(input())

for i in range(N):
    a = input().lower()
    print(a)

