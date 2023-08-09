N = int(input())
a = '* '
b = ' *'
if N == 1:
    print('*')
elif N%2==1:
    for _ in range(N//2):
        print(f'{a*(N-1)}*\n{b*N}')
    print(f'{a*(N-1)}*')
else:
    for _ in range(N//2):
        print(f'{a*(N-1)}*\n{b*N}')