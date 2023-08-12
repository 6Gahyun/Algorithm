A, B, C = map(int, input().split())
num = [0] * 100
for _ in range(3):
    t1, t2 = map(int, input().split())
    for i in range(t1, t2):
        num[i-1] += 1
total = 0
for i in num:
    if i == 1:
        total += i*A
    elif i == 2:
        total += i*B
    elif i == 3:
        total += i*C
print(total)