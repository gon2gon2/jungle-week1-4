# strip이 문제였다. 총 15분
import sys
input = sys.stdin.readline
left = list(input().strip())
N = int(input())

right = []
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "P":
        left.append(cmd[1])
    elif cmd[0] == "L":
        if not left:
            continue
        x = left.pop()
        right.append(x)
    elif cmd[0] == "D":
        if not right:
            continue
        x = right.pop()
        left.append(x)
    else:
        if left:
            left.pop()
        else:
            continue
right.reverse()
print("".join(left+right))