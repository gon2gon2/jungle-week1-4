# 평가: 이전에 구한 값을 어ㄸ떻게 활용해야 하는지 떠올리는 게 관건
import sys

input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input()) # 동전 가짓수
    coin = [*map(int,input().split())] # 동전들, 오름차순
    M = int(input()) # 만들어야 되는 금액
    
    dp = [0] * (M+1)
    dp[0] = 1
    '''
    [현재 금액 - 동전]의 값을 더해줌
    동전 개수 하나만 추가한다면 똑같이 재현이 가능한 것이므로.
    
    '''
    
    for i in range(N):
        for j in range(coin[i], M+1):
            dp[j] += dp[j - coin[i]]

    print(dp[M])
