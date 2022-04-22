# 시작: 23:08
# 종료: 23:24
# 평가: 얼떨결에 풀이를 들어서 쉽게 해결
import sys

input = sys.stdin.readline


N = int(input())

house = [[*map(int, input().split())] for _ in range(N)]


for i in range(1,N):
    for j in range(3):
        candi =  [*set(range(3)) - set([j])]
        house[i][j] += min(house[i-1][candi[0]], house[i-1][candi[1]])


print(min(house[-1]))

        

