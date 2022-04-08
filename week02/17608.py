import sys
input = sys.stdin.readline

N = int(input())
stack = [int(input()) for _ in range(N)]

temp = 0
cnt = 0
for _ in range(N):
    p = stack.pop()
    if p > temp:
        temp = p
        cnt += 1

print(cnt)


