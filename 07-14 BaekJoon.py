#!/usr/bin/env python
# coding: utf-8

# ##### #1225 이상한 곱셈

# In[16]:


# 처음에 생각한 방법 --> 시간초과
a, b = map(str, input().split())
c=[]
for i in range(len(a)):
    for j in range(len(b)):
        c.append(int(a[i])*int(b[j]))
sum(c)


# In[21]:


a, b = map(str, input().split())
a_list = list(map(int, a))
b_list = list(map(int, b))
print(sum(a_list) * sum(b_list))


# ##### #1526 가장 큰 금민수

# In[4]:


N = int(input())
while True:
    a = True
    for i in str(N):
        if i != '4' and i != '7':
            a = False
            N = N-1
    if a:
        print(N)            
        break


# In[9]:


N = int(input())
n_list = list(map(int, input().split()))
v = int(input())
print(n_list.count(v))

