N = input()
res = 'NO'


for i in range(len(N)-1):
    a, b = 1, 1
    if i+1 == len(N):
        break
    else:
        a = map(int, N[:i+1])
        b = map(int, N[i+1:])
        c = 1
        d = 1
        for i in a:
            c *= i
        for j in b:
            d *= j
        if c == d:
            res = 'YES'
print(res)