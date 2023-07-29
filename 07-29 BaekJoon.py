#!/usr/bin/env python
# coding: utf-8

# ### 2739 구구단

# In[4]:


N = int(input())
for i in range(1, 10):          # 1부터 9까지
    print(f'{N} * {i} = {N*i}') # 


# ### 1330 두 수 비교하기

# In[8]:


a, b = map(int, input().split())
if a<b:
    print('<')
elif a>b:
    print('>')
else:
    print('==')


# ### 9498 시험 성적

# In[9]:


s = int(input())
if s >= 90:
    print('A')
elif s >= 80:
    print('B')
elif s >= 70:
    print('C')
elif s >= 60:
    print('D')
else:
    print('F')


# ### 2753 윤년

# In[12]:


y = int(input())
if (y%4==0 and y%100!=0) or (y%400==0):
    print(1)
else:
    print(0)


# ### 14681 사분면 고르기

# In[17]:


x = int(input())
y = int(input())

if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)


# ### 2884 알람 시계

# In[54]:


H, M = map(int, input().split())

if H==0:
    H=24

time = (H*60 + M) - 45
hour = time//60
minute = time%60
    
print(hour, minute)


# In[55]:


H, M = map(int, input().split())

if H==0:
    H=24

time = (H*60 + M) - 45
hour = time//60
minute = time%60

if hour == 24:
    hour=0

print(hour, minute)


# ### 2525 오븐 시계

# In[45]:


A, B = map(int, input().split())
C = int(input())

hour = A + (B+C)//60
minute = (B+C)%60

if hour >= 24:
    hour -= 24

print(hour, minute)


# ### 2480 주사위 세 개

# In[50]:


a, b, c = map(int, input().split())
if a==b==c:
    print(10000+a*1000)
elif a==b or a==c:
    print(1000+a*100)
elif b==c:
    print(1000+100*c)
else:
    print(max(a, b, c)*100)

