# 시작: 17:12
# 종료: 17:26
# 평가: 
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coin = [int(input()) for _ in range(N)]
ans = 0
for c in coin[::-1]:
    if not K:
        break
    if c>K:
        continue
    ans += K//c
    K = K%c

print(ans)
