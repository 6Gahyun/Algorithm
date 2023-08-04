#!/usr/bin/env python
# coding: utf-8

# ### 2675 문자열 반복

# In[20]:


T = int(input())
for i in range(T):
    R, S = input().split()
    for s in S:
        print(f'{s*int(R)}', end='')
    print()

