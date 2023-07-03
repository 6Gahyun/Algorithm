#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 2753
y = int(input())
if y%4 == 0 and (y%100!=0 or y%400 ==0):
    print(1)
else:
    print(0)


# In[14]:


# 14681
x, y = map(int, input().split())
if x > 0 and y > 0:
    print(1)
elif x > 0  and y < 0:
    print(4)
elif x < 0 and y > 0:
    print(2)
else:
    print(3)


# In[27]:


n = int(input())
for i in range(1, n+1):
    print((''*' * i).rjust()
for i in range(1, n):
    print(('*' * (n-i)).rjust())


# In[54]:


n = int(input())
for i in range(1, n+1):
    print(('*' * (2*(n-i)+1)).center(2*n-1).rstrip())
for i in range(2, n+1):
    print(('*' * (2*i-1)).center(2*n).rstrip())


# In[62]:


n = int(input())
for i in range(1, n):
    print('*'*i, ' '*2*(n-i), '*'*i)
for j in range(n, 0, -1):
    print('*' * j, ' '*2*(n-j), '*' * j)
    
n = int(input())
for i in range(1, n):
    print('*'*i + ' '*2*(n-i) + '*'*i)
for i in range(n, 0, -1):
    print('*'*i + ' '*2*(n-i) + '*'*i)


# In[5]:


# 1924
x, y = map(int, input().split())
m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day = 0
for i in range(x-1):
    day += m[i]
day = (day+y)%7
print(d[day])


# In[8]:


#3052
arr = []
for i in range(10):
    a = int(input())
    if a%42 not in arr:
        arr.append(a%42)
print(len(arr))


# In[11]:


# 27866
S = input()
i = int(input())
print(S[i-1])


# In[12]:


# 2743
a = input()
print(len(a))


# In[16]:


# 9086
T = int(input())
for i in range(T):
    a = str(input())
    print(a[0]+a[-1])


# In[24]:


print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \\. \". L_r'")
print("   `~\\/")
print("      |")
print("      |")

