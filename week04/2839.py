# 시작: 20:07
# 종료: 20:28
# 평가: DP를 많이 접해보지 않아서 그런지 어렵다. 풀이를 검색했다.
import sys

input = sys.stdin.readline

N = int(input())
dp = [9999] * 5001
dp[3] = dp[5] = 1

for i in range(6,N+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

print(dp[N] if dp[N] < 9999 else -1)
