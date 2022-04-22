# 시작: 16:55
# 종료:
# 평가:
import sys

input = sys.stdin.readline

N = int(input())


dp = [0,1] + [0]*N

for i in range(2,N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])
