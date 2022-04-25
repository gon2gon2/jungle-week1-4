# 시작: 16:50
# 종료: 
# 평가: 인덱싱이 복잡해서 분명 실수할 것 같다.
import sys

input = sys.stdin.readline

seq_1 = input().strip()
seq_2 = input().strip()

n_1 = len(seq_1)
n_2 = len(seq_2)

dp = [[0]*(n_2+1) for _ in range(n_1+1)]

for i in range(1, n_1+1):
    for j in range(1, n_2+1):
        if seq_1[i-1] == seq_2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
        
