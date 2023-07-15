#!/usr/bin/env python
# coding: utf-8

# ##### #3003 킹, 퀸, 룩, 비숍, 나이트, 폰

# In[16]:


N = list(map(int, input().split()))
A = [1, 1, 2, 2, 2, 8]
dif = []
for i in range(len(N)):
    print(A[i] - N[i], end=' ')


# ##### #1476 날짜 계산

# In[ ]:


e, s, m = map(int, input().split())
E, S, M, year = 0, 0, 0, 0

while True:
    E, S, M, year = E+1, S+1, M+1, year+1

    if 15 < E:
        E=1
    if 28 < S:
        S=1
    if 19 < M:
        M=1
    

    if (e==E) and (s==S) and (m==M):
        break

print(year)


# ##### #2563 색종이

# In[2]:


paper = [[0 for _ in range(100)] for _ in range(100)]
color_paper_num = int(input())

for i in range(color_paper_num):
    left, bottom = map(int, input().split())
    for y in range(bottom, bottom+10):
        for x in range(left, left+10):
            paper[y][x] = 1

total=0
for i in range(100):
    total+=paper[i].count(1)

print(total)
        

