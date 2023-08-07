#!/usr/bin/env python
# coding: utf-8

# ### #1436 영화감독 숌

# In[ ]:


N = int(input())

title = 666
while N != 0:
    if '666' in str(title):
        N-=1
        if N==0:
            break
    title += 1
print(title)


# In[ ]:


n = int(input())
# N번째 영화
lst =[]
k = 665
while len(lst)<n : 
# lst 요소의 개수가 영화 시리즈 수보다 작은 동안 반복
    str_k = str(k)
    # 666의 존재 유무를 비교하기 위해 문자열로 변환
    if '666'in str_k:
    # str_k 문자열에 666이 있다면, 
        lst.append(k)
        # lst에 666이 포함된 k 추가하기
    k = k+1
    # k를 1씩 증가시키면서
print(lst.pop())
# 선입후출 : 리스트의 가장 최근에 들어간 요소 빼기


# ### #2309 일곱 난쟁이

# In[27]:


height = []

for _ in range(9):
    a = int(input())
    height.append(a)
total_height = sum(height)
check=True
for i in range(9):
    for j in range(i+1, 9):
        c = height[i]
        b = height[j]
        if total_height-(c+b)==100:
            height.remove(c)
            height.remove(b)
            check=False
            break
    if check==False:
        break
height.sort()
print(*height, sep='\n')

