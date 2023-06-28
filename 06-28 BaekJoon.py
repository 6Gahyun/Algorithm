#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 백준 2480번 주사위 문제 풀이
a, b, c = map(int, input().split())

if (a == b) and (a == c):
    print(10000 + a * 1000)
elif (a == b) or (a == c):
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)


# In[11]:


# 백준 10699번 오늘 날짜 출력 
import datetime
date = datetime.datetime.utcnow()
print(date.strftime('%Y-%m-%d'))

