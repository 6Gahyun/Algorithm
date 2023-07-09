#!/usr/bin/env python
# coding: utf-8

# ##### #2839 설탕 배달
# https://www.acmicpc.net/problem/2839

# In[ ]:


n = N//5
1. 5*n = N
2. (N-5*n)%3 == 0
3. N


# In[15]:


N = int(input())
n = N//5

if N%5 == 0:
    print(int(N/5))
else:
    if (N-5*n)%3 == 0:
        print(int(n+(N-5*n)/3))
    elif N%3==0:
        print(int(N/3))
    else:
        print(-1)

# 이렇게 하면 11kg 계산이 안됨!


# In[25]:


N = int(input())
p=0 # N에서 3kg을 빼면 설탕 가방 +1해줌
if N%5 == 0:
    print(N//5)
else:
    while N>0:
        N-=3
        p+=1
        if N%5==0:
            p+=N//5
            print(p)
            break
        elif N%3==0:
            print(N//3)
            break
        else:
            print(-1)
            break
# 이 경우도 9kg이 이상해짐 


# In[26]:


N = int(input())
p=0 # N에서 3kg을 빼면 설탕 가방 +1해줌
if N%5 == 0:
    print(N//5)
else:
    while N>0:
        N-=3
        p+=1
        if N%5==0:
            p+=N//5
            print(p)
            break
        elif N%3==0:
            p+=N//3
            print(p)
            break
        else:
            print(-1)
            break


# In[30]:


N = int(input())
p=0 # N에서 3kg을 빼면 설탕 가방 +1해줌
if N%5 == 0:
    print(N//5)
else:
    while N>0:
        N-=3
        p+=1
        if N%5==0:
            p+=N//5
            print(p)
            break
        elif N==1 or N==2:
            print(-1)
            break
        elif N==0:
            print(p)
            break


# ##### #1476 날짜 계산
# https://www.acmicpc.net/problem/1476

# ###### year = 1 E=1 S=1 M=1
# ###### year = 2 E=2 S=2 M=2
# ###### year = 15 E=15 S=15 M=15
# ###### year = 16 E=1 S=16 M=16
# ###### year = 20 E=5 S=20 M=1
# 

# In[4]:


E, S, M = map(int, input().split())

year = 1
while True:
    if (year-E)%15==0 and (year-S)%15==0 and (year-M)%15==0:
        break
    year += 1
    
print(year)


# ##### #2490 윷놀이

# In[2]:


for _ in range(3):
    a = list(map(int, input().split()))
    if a.count(0) == 4:
        print('D')
    elif a.count(0) == 3:
        print('C')
    elif a.count(0) == 2:
        print('B')
    elif a.count(0) == 1:
        print('A')
    else:
        print('E')


# ##### #2562 최댓값

# In[7]:


N = []
for _ in range(9):
    n = int(input())
    N.append(n)

print(max(N))
print(N.index(max(N))+1)


# ##### #2953 나는 요리사다.

# In[1]:


s = []
for i in range(5):
    a = list(map(int, input().split()))
    s.append(sum(a))
print(s.index(max(s))+1, max(s), end=' ')


# ##### #1453 피시방 알바

# In[5]:


N = int(input())
num = list(map(int, input().split()))

count = 0
seat = []
for n in range(N):
    if num[n] in seat:
        count += 1
    else:
        seat.append(num[n])
print(count)

