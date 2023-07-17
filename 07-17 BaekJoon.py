#!/usr/bin/env python
# coding: utf-8

# #2083 럭비클럽

# In[ ]:


while True:
    name, age, weight = input().split()
    if '#' in name:
        break
    if int(age) >17 or int(weight)>=80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')


# #1271 엄청난 부자2

# In[4]:


n, m = map(int, input().split())
print(n//m, n%m, sep='\n')


# #2338 긴자리계산

# In[9]:


A = int(input())
B = int(input())
print(A+B, A-B, A*B, sep='\n')


# #2742

# In[13]:


N = int(input())
for i in range(N, 0, -1):
    print(i)


# #

# #2845

# In[19]:


L, P = map(int,input().split())
a = list(map(int, input().split()))
total = L*P
for i in range(5):
    print(a[i]-total, end=' ')

