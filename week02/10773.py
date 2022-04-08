import sys
input = sys.stdin.readline

K = int(input())
stack = []
for _ in range(K):
    x = int(input())
    if not x:
        stack.pop()
    else:
        stack.append(x)


print(sum(stack))
