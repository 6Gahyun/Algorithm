n, m = map(int, input().split(' '))
mat1 = []
mat2 = []
mat3 = [[0 for j in range(m)] for i in range(n)]

for row in range(n):
    col = list(map(int, input().split()))
    mat1.append(col)
for row in range(n):
    col = list(map(int, input().split()))
    mat2.append(col)

for row in range(n):
    for col in range(m):
        mat3[row][col] = mat1[row][col] + mat2[row][col]

for row in range(n):
    for col in range(m):
        print(mat3[row][col], end=' ')
    print()