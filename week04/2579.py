# 시작: 16:03
# 종료:
# 평가: 처음에 대충 비슷하게 떠올리긴 했는데, 연속 3개가 아니라는 부분을 좀 더 생각했어야 됐다.
import sys

input = sys.stdin.readline


N = int(input())

#score_list = [0] + [int(input()) for _ in range(N)]
#
#dp = score_list[:3] + [0] * N
#dp[2] += dp[1]
#for i in range(3,N+1):
#    dp[i] = max(dp[i-2], dp[i-3]) + score_list[i]

score_list = [0] * 301
for i in range(N):
    score_list[i] = int(input())

dp = [0] *(N+3)
dp[0] = score_list[0]
dp[1] = score_list[1] + score_list[0]
dp[2] = max(score_list[0] + score_list[2], score_list[1]+ score_list[2])
for i in range(3, N):
    dp[i] = max(dp[i-3]+score_list[i-1], dp[i-2]) + score_list[i]

print(dp[N-1])




