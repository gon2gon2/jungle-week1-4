# 시작: 17:10
# 종료: 17:25
# 평가: 전에 LIS 공부를 해놔서 빨리 끝냄
import sys

input = sys.stdin.readline

N = int(input())
numbers = [*map(int, input().split())]
DP = [1] * N

for i in range(N):
    for j in range(i):
        if numbers[j] < numbers[i]:
            DP[i] = max(DP[j]+1, DP[i])
print(max(DP))
