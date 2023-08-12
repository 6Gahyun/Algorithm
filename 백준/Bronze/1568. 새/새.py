# 새의 수 N
N = int(input())
k = 1 # 노래할 숫자,
num = 0
while N > 0:
    if k > N: # 숫자 차례, 남은 새의 수가 불러야하는 숫자보다 작은 경우
        k = 1 # 자연수 1로 돌아가
    N-=k
    # 1부터 모든 자연수 오름차순
    k+=1
    num += 1
print(num)