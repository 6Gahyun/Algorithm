#!/usr/bin/env python
# coding: utf-8

# #### #1546 평균

# In[13]:


n = int(input())
score = list(map(int, input().split()))
S = max(score)
new_score = []
for i in score:
    new_score.append(i/S*100)
print(sum(new_score)/len(new_score))


# #### #1934 최소공배수

# In[16]:


import math
 
t = int(input())
for i in range(t):
  a, b = map(int, input().split())
  print(math.lcm(a, b))

