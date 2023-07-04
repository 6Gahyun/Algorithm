#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 11654 주어진 글자의 아스키 코드 출력
a = input()
print(ord(a))


# In[13]:


# 1157 입력받은 단어 중 가장 많이 등장하는 알파벳 출력
w = input().upper()
w_list = list(set(w))
cnt = []

for i in w_list:
    cnt.append(w.count(i))
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(w_list[cnt.index(max(cnt))])


# In[23]:


# 5086 배수와 약수
# while 반복문으로 무한 루프 만들기
while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break

    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')


# In[11]:


# 2720 거스름돈 계산

n = int(input())
for i in range(n):
    S = int(input())
    S_list = []
    for i in [25, 10, 5, 1]:
        S_list.append(S//i)
        S = S%i
    print(*S_list)

