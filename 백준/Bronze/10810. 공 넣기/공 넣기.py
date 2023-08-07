N, M = map(int, input().split())
num = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    for a in range(i, j+1):
        num[a-1] = k
for i in range(N):
    print(num[i], end = ' ')