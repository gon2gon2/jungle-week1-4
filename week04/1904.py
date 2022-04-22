# 시작: 16:25
# 종료: 17:05
# 평가: 쉬운 문제를 해결하지 못했다. 쉽게 쉽게 생각하자.
import sys

input = sys.stdin.readline

N = int(input())
D = 15746
dp = [0,1,2] + [0] * 1000001
for i in range(3,N+1):
    dp[i] = (dp[i-1] + dp[i-2])%D
print(dp[N])

