# 속도 개선
# 3976 -> 140
# 방법: input 대신 readline사용

import sys
input = sys.stdin.readline

N = int(input())
ropes = sorted([int(input()) for _ in range(N)])

ans = 0

for i in range(N):
    maximmum = ropes[i] * (N-i)

    if maximmum > ans:
        ans = maximmum

print(ans)
