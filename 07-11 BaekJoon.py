#!/usr/bin/env python
# coding: utf-8

# ##### #1269 대칭차집합

# In[10]:


A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(set(a)^set(b))
print(len(c))


# ##### #19532 수학은 비대면강의입니다.

# In[14]:


a, b, c, d, e, f = map(int, input().split())
result = False
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x + b*y == c) and (d*x + e*y == f):
            result = True
            break
    if result == True:
        break

print(x, y)


# ##### #1427 소트인사이드

# In[40]:


N = int(input())
n_list = list(map(int, str(N)))
n_list.sort(reverse=True)
n = ''.join(map(str, n_list))
n = int(n)
print(n)


# ##### #9506 약수들의 합

# In[46]:


while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    for i in range(1, n):
        if n%i == 0:
            arr.append(i)
    if sum(arr) == n:
        print('%s = '%n, ' + '.join(str(i) for i in arr), sep='')
    else:
        print('%s is NOT perfect.'%n)

