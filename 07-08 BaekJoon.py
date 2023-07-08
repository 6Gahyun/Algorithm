#!/usr/bin/env python
# coding: utf-8

# ##### #2525 오븐시계

# In[2]:


hour, minute = map(int, input().split(' '))
cooking_minute = int(input())

final_minute = (hour * 60) + minute + cooking_minute # 현재시간 + 입력받은 요리시간 다 분으로 더함
final_hour = (final_minute //60) % 24 # 최종 분을 60으로 나눈 몫 "시간" 그걸 24로 나눈다는 것은 00시도 있기 때문
final_minute = final_minute % 60

print(final_hour, final_minute)


# In[4]:


import sys

H, M = map(int,sys.stdin.readline().split())
ah,am = 0,0
if M<45:
    am = 60+M-45
else:
    am = M-45
ah = H
if (M-45) < 0:
    ah -=1
if ah < 0:
    ah = 24+ah
print(ah,am)


# ##### #2445 별찍기 8

# In[3]:


n = int(input()) # 5 입력, 중간 줄 10개 출력
for i in range(1, 2*n): # i 1~9
    col = 2 * n 
    star = n - abs(n-i)
    l = '*' * star + ' ' * (col-2*star) + '*' * star
    print(l)
# n이 1 ~ 9까지 반복할 때 절댓값을 이용해서 1,2,3,4,5,4,3,2,1 반복할 수 있도록


# ##### #10807 개수세기
# https://www.acmicpc.net/problem/10807

# In[16]:


N = int(input())
n_list = list(map(int, input().split()))
v = int(input())

print(n_list.count(v))


# ##### #2738 행렬덧셈
# https://www.acmicpc.net/problem/2738

# In[ ]:


# 행렬 덧셈
n, m = map(int, input().split(' '))
mat1 = []
mat2 = []
mat3 = [[0 for j in range(m)] for i in range(n)]
# 입력
for row in range(n):
    col = list(map(int, input().split()))
    mat1.append(col)
for row in range(n):
    col = list(map(int, input().split()))
    mat2.append(col)
# 더하기
for row in range(n):
    for col in range(m):
        mat3[row][col] = mat1[row][col] + mat2[row][col]
# 출력
for row in range(n):
    for col in range(m):
        print(mat3[row][col], end=' ')
    print()


# In[1]:


# 수 정렬하기
n = int(input())
arr = list(map(int, input().split()))
print("Input", arr)

for i in range(n - 1):
    min_idx = i
    for j in range(i+1, n):
        if arr[min_idx] > arr[j]:
            min_idx = j
    print(i + 1, "번째 작은 수: ", arr[min_idx], "--->", sep='', end='')
    # swap
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr)
print("Output", arr)


# ##### #10871 X보다 작은 수
# https://www.acmicpc.net/problem/10871

# In[2]:


N, X = map(int, input().split())
num = list(map(int, input().split()))

for i in range(N):
    if num[i] < X:
        print(num[i], end=' ')


# ##### #10810 공 넣기
# https://www.acmicpc.net/problem/10810

# In[14]:


N, M = map(int, input().split())
num = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    for a in range(i, j+1):
        num[a-1] = k
for i in range(N):
    print(num[i], end = ' ')


# ##### #10813 공 바꾸기
# - N : 바구니 개수
# - M : 공을 바꾸는 횟수

# In[18]:


N, M = map(int, input().split())
num = []
for i in range(1, N+1):
    num.append(i)

for m in range(M):
    i, j = map(int, input().split())
    num[i-1], num[j-1] = num[j-1], num[i-1]

for i in range(N):
    print(num[i], end=' ')


# ##### #2798 블랙잭
# https://www.acmicpc.net/problem/2798

# In[20]:


N, M = map(int, input().split())
num = list(map(int, input().split()))
result = 0
max = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if num[i]+num[j]+num[k] > M:
                continue
            else:
                result = num[i]+num[j]+num[k]
                if max <= result:
                    max = result
print(max)


# ##### #1436 영화감독 숌
# - 브루트포스 <br>
# https://www.acmicpc.net/problem/1436

# In[24]:


N = int(input())
print(str(N-1)+'666')


# In[23]:


N = int(input())

title = 666
while N != 0:
    if '666' in str(title):
        N-=1
        if N==0:
            break
    title += 1
print(title)


# ##### #2750 수 정렬하기
# https://www.acmicpc.net/problem/2750

# In[ ]:


N = int(input())
lst1 = []
for i in range(N):
    lst1.append(int(input()))
lst1.sort()
for i in range(len(lst1)):
    print(lst1[i])


# ##### #2751 수 정렬하기2

# ##### #2309 일곱 난쟁이
# https://www.acmicpc.net/problem/2309
# - 전체 키 총합에서 난쟁이가 아닌 두 개의 키값을 뺐을 때 100이 되어야함

# In[31]:


height_list = []
height_sum = 0
# 난장이들의 키 값 입력받기 
for i in range(9):
    height = int(input())
    height_sum += height
    height_list.append(height)

# 키 정렬
height_list.sort()

# 두 난장이의 가능한 인덱스값 모두 출력
is_ok = False # 오류를 막기 위해 정답을 찾았을 때 로직을 멈추기 위한 변수 
# is_ok 변수가 없을 때 발생하는 오류
# 만약 중간에 답을 찾은 경우, remove를 이용해서 값을 제거했음
# 하지만 인덱스 값의 경우 0~8까지 받았잖아,, 실제 리스트에는 remove를 통해 값이 제거되어 인덱스 값이 적은데 8번째 인덱스값을 찾아라 하면 당연히 오류가 생긴다잉
for first in range(9):
    for second in range(9):
        if first == second:
            continue
        height_total = height_sum - height_list[first] - height_list[second]
        if height_total == 100:
            height_list.remove(height_list[second])
            height_list.remove(height_list[first])
            is_ok = True
            break

    if is_ok:
        break
for height in height_list:
    print(height)

