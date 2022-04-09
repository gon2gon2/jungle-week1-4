import sys
input = sys.stdin.readline
string = list(input().strip())

stack = []
answer = 0
temp = 1

for i in range(len(string)):
    # "("
    if string[i] == '(':
        stack.append("(")
        temp *= 2

    # "["
    elif string[i] == '[':
        stack.append("[")
        temp *= 3

    # ")"
    elif string[i] == ')':
        if not stack or stack[-1] != "(":
            answer = 0
            break

        if string[i-1] == "(":
            answer += temp
        temp //= 2
        stack.pop()

    # "]"
    else:
        if not stack or stack[-1] != "[":
            answer = 0
            break
        if string[i-1] == "[":
            answer += temp
        temp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(answer)

