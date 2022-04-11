# 25분 걸렸음 -> 시간초과(그럴 거 같았음, n^2)
# import sys
# input = sys.stdin.readline
# N = int(input())
# stack = [*map(int,input().strip().split())]
# popped = []
# ans = []

# for _ in range(N):
#     x = stack.pop()
#     popped.append(x)

#     for i in range(-1, -len(popped)-1, -1):
#         if x < popped[i]:
#             ans.append(popped[i])
#             break
#     else:
#         ans.append(-1)
            
# print(*ans[::-1])

# 스택의 활용이 참 어렵다. while pop하는 부분을 많이 해야될듯 탑문제도 그렇고 

import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int, sys.stdin.readline().strip().split()))
answer = [-1] * n
stack = [0]


for i in range(1, n):
    while stack and numbers[i] > numbers[stack[-1]]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)
print(*answer)