n = int(input())
num = [0, 1]

if n==0:
    print(0)
elif n==1:
    print(1)
else:
    for _ in range(n-1):
        num.append(num[-1]+num[-2])
    print(num[n])