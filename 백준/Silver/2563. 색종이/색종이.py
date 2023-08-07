paper = [[0 for _ in range(100)] for _ in range(100)]
color_paper_num = int(input())

for i in range(color_paper_num):
    left, bottom = map(int, input().split())
    for y in range(bottom, bottom+10):
        for x in range(left, left+10):
            paper[y][x] = 1

total=0
for i in range(100):
    total+=paper[i].count(1)

print(total)