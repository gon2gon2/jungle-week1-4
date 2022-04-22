# 시작: 20:31
# 종료: 20:55
# 평가: 그래도 얼추 비슷하게는 했다. 
import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N+3)
dp[2] = dp[3] = 1
for i in range(4, N+1):
    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

    elif i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[N])
