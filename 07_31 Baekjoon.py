#!/usr/bin/env python
# coding: utf-8

# #### 10950 A + B -3

# N = int(input())
# for i in range(N):
#     A, B = map(int, input().split())
#     print(A+B)

# #### 8393 합 

# In[8]:


N = int(input())
sum=0
for i in range(1, N+1):
    sum+=i
print(sum)


# #### 25304 영수증

# In[11]:


X = int(input())
N = int(input())
total = 0
for i in range(N):
    a, b = map(int, input().split())
    c = a*b
    total+=c
if total == X:
    print('Yes')
else:
    print('No')


# #### 25314 코딩은 체육과목

# In[16]:


N = int(input())
x = N//4
print('long'*x, 'int', end=' ')


# #### 15552 빠른 A+B

# In[24]:


import sys
T = int(input())
for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A+B)


# #### 11021 A + B -7

# In[20]:


T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(f'Case #{i+1}: {A+B}')


# #### 11022 A + B -8

# In[21]:


T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(f'Case #{i+1}: {A} + {B} = {A+B}')


# #### 2438 별 찍기 -1

# In[25]:


N = int(input())
for i in range(1, N+1):
    print('*' * i)


# #### 2439 별 찍기 -2

# In[ ]:


N = int(input())
for i in range(1, N+1):
    print('*' * i, align=center) # 중앙정렬


# #### 10952 A + B -5

# In[ ]:


while True:
    A, B = map(int, input().split())
    print(A+B)
    if A == 0 and B == 0:
        break

