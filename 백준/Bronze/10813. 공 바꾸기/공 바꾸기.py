N, M = map(int, input().split())
num = []
for i in range(1, N+1):
    num.append(i)

for m in range(M):
    i, j = map(int, input().split())
    num[i-1], num[j-1] = num[j-1], num[i-1]

for i in range(N):
    print(num[i], end=' ')
