# 31분: 시간도 빨라지고 코드도 간결해졌다
N = int(input())
tower = list(map(int,input().split()))
ans = [0] * N

stack = [0]

for i in range(1, N):

    while stack and tower[stack[-1]] < tower[i]:
        stack.pop()
    if stack and tower[stack[-1]] > tower[i]:
        ans[i] = stack[-1] + 1
    stack.append(i)

print(*ans)