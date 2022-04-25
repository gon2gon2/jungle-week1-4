# 시작: 18:30
# 종료: 20:40
# 평가: knapsack 알고리즘에 대해 공부하느라 시간이 좀 걸렸다. 
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# [무게, 가치]
stuff = [[0,0]]+[[*map(int, input().split())] for _ in range(N)]



dp = [[0]*(K+1) for _ in range(N+1)]

print(stuff)
print(dp)

for i in range(1, N+1):     # 물건 id
    for w in range(1, K+1): # 담을 수 있는 용량
        

        # 배낭에 더 못 넣는 경우
        if stuff[i][0] > w:
            dp[i][w] = dp[i-1][w]

        # 더 넣을 수 있는 경우
        else:
            dp[i][w] = max(dp[i-1][w], stuff[i][1] + dp[i-1][w-stuff[i][0]])
print(dp[-1][-1]) 
