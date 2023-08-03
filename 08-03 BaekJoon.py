#!/usr/bin/env python
# coding: utf-8

# ### 1085 직사각형에서 탈출

# In[5]:


x, y, w, h = map(int, input().split())
lst = [h-y, w-x, y, x]
print(min(lst))


# ### 10811 바구니 뒤집기

# In[45]:


N, M = map(int, input().split())
basket = [x+1 for x in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

print(*basket)

