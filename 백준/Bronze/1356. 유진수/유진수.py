N = input()
res = 'NO'

for k in range(1,len(N)):
    a = N[:k]
    b = N[k:]

    c=1
    d=1
    for i in a:
        c *= int(i)
    for j in b:
        d *= int(j)

    if c==d:
        res = 'YES'
print(res)