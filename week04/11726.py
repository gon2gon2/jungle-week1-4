# 시작: 22:35
# 종료: 22:45
# 평가: append로 추가해주나 인덱싱해서 넣어주나 똑같이 나오긴 했다. 나중에 다른 문제에서도 테스트해봐야지
# 이렇게 풀리는 게 맞나 싶다 대충 찍어본건데...
import sys
input = sys.stdin.readline

N = int(input())
D = 10007
dp = [0,1,2] + [0]*(N+1)


for i in range(3, N+1):
    dp[i]=(dp[i-1]+dp[i-2])%D
print(dp[N])
