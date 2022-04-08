import sys
input = sys.stdin.readline


def check_parenthesis(x:str):
    stack = []
    for s in x:
        if s == "(" or s == "[":
            stack.append(s)

        elif s == ')':
            if not stack:
                return "NO"
            p = stack.pop()
            if p != "(":
                return "NO"


        elif s == "]":
            if not stack:
                return "NO"
            p = stack.pop()
            if p != "[":
                return "NO"
    if stack:
        return "NO"
    return "YES"

T = int(input())

for _ in range(T):
    print(check_parenthesis(input()))
