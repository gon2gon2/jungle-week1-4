# 시작: 20:43
# 종료:
# 평가: 재밌는 문제였다. 바텀업으로 구할 수 있는 것 부터 구해나가는 모습이 왠지 감동적이다.
import sys

input = sys.stdin.readline

N = int(input())
matrix = [[*map(int, input().split())] for _ in range(N)]
dp = [[0]*N for _ in range(N)]

for diagonal in range(1, N):
    for i in range(0, N-diagonal):
        j = i + diagonal
        
        if diagonal == 1:
            dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1]
            continue

        dp[i][j] = float('inf')

        for k in range(i, j):
            dp[i][j] = min(
                        dp[i][j], 
                        dp[i][k] + dp[k+1][j] + matrix[i][0] *matrix[k][1] * matrix[j][1]
                    )

print(dp[0][N-1])
        



