# 키로거
# 소요시간 12분
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    script = list(input().strip())
    left  = []
    right = []
    for cmd in script:

        if cmd == '-':
            if not left:
                continue
            left.pop()

        elif cmd == '<':
            if not left:
                continue
            x = left.pop()
            right.append(x)
            

        elif cmd == '>':
            if not right:
                continue
            x = right.pop()
            left.append(x)
        else:
            left.append(cmd)


    print(''.join(left+right[::-1]))