#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 2501
# https://www.acmicpc.net/problem/2501
N, K = map(int, input().split())
N_list = []
for i in range(1, N+1):
    if N%i==0:
        N_list.append(i)

if len(N_list) < K:
    print(0)
else:
    print(N_list[K-1])

