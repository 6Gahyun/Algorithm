A, B = map(int, input().split())
C = int(input())
minute = B+C

if minute>=60:
    if minute%60==0:
        A += minute//60
        B = 0
    else:
        A+=minute//60
        B=minute%60
else:
    B = minute

if A >= 24:
    A-=24

print(A, B)