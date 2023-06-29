#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 백준 문제풀이 2588 곱셈
# https://www.acmicpc.net/problem/2588
a = int(input())
b = input() 
b_list = list(map(int, b))
# 정수형을 문자열로 바꾼 후 map 함수를 이용해 슬라이싱, 리스트 형태로 만들어줌
print(a * b_list[2])
print(a * b_list[1])
print(a * b_list[0])
print(a * int(b))


# In[2]:


# 백준 문제풀이 18108
# https://www.acmicpc.net/problem/18108
y = int(input())
print(y-543)


# In[ ]:


# 백준 문제풀이 5597
# https://www.acmicpc.net/problem/5597
stu = [i for i in range(1, 31)]

for _ in range(28):
    attendance = int(input())
    stu.remove(attendance)
    
print(min(stu))
print(max(stu))

