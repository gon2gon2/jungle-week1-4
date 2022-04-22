# 평가: 규칙을 모르겠다면 경우의 수를 잘 세었는지 생각해보자..
import sys

input = sys.stdin.readline

T = int(input())
numbers = [int(input()) for t in range(T)]

dp = [0,1,2,4]

for i in range(4, max(numbers)+1):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for n in numbers:
    print(dp[n])


