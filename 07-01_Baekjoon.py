#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
list_in_list = list()
n = int(input())
for i in range(n):
    list_in_list.append(list(map(int, sys.stdin.readline().split())))
print(list_in_list)


# In[5]:


print("hi") # hi
print() #\n
print("hello", "my", "name", "is") # hello my name is
print("hi", end="") 
print("hello", "my", "name", "is", sep="")
print("hello", "my", "name", "is", sep="\n")


# In[14]:


N = int(input())
if N%2 == 0:
    print('짝수')
else:
    print('홀수')


# In[15]:


# 9498
s = int(input())
if s >=90:
    print("A")
elif s >=80:
    print("B")
elif s >=70:
    print("C")
elif s >=60:
    print("D")
else:
    print("F")


# In[20]:


# 8393
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)


# In[24]:


# 10818
N = int(input())
N_list = list(map(int, input().split()))
print(min(N_list), max(N_list))


# In[28]:


# 1330
A, B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')


# In[34]:


# 2438
n = int(input())
for i in range(1, n+1):
    print('*' * i)


# In[36]:


# 2439
n = int(input())
for i in range(1, n+1):
    print(('*' * i).rjust(n))


# In[42]:


# 2440
n = int(input())
for i in range(0, n+1):
    print('*' * (n-i))


# In[46]:


# 2441
n = int(input())
for i in range(0, n+1):
    print(('*' * (n-i)).rjust(n))


# In[4]:


# 2442
n = int(input())
for i in range(0, n):
    print(('*' * (2*i+1)).center(2*n-1).rstrip())


# In[18]:


# 25314
n = int(input())
for i in range(n//4):
    print('long', end = ' ')
print('int')


# In[7]:


# 2443
a = int(input())
for i in range(0, a):
    print(('*' * (2*(a-i)-1)).center(2*a).rstrip())


# In[31]:


# 2444
n = int(input())
for i in range(0, n):
    print(('*' * (2*i+1)).center(2*n+1).rstrip())
for i in range(0, n-1):
    print(('*' * (2*(a-i)-3)).center(2*n+1).rstrip())


# In[57]:


# 2525
a, b = map(int, input().split())
c = int(input())
h = c // 60
m = c % 60
if b+c<60:
    h = a+h
    m = b + m
elif (b+c)%60==0:
    h = a + ((b+c)// 60)
    m = 0
else:
    h = a + ((b+c)// 60)
    m = b + ((b+c)%60)
print(h, m)


# In[1]:


# 2884
h, m = map(int, input().split())

if m < 45:
    if h == 0:
        h = 23
        m += 15
    else:
        h -= 1
        m += 15
else:
    m -= 45
print(h, m)

