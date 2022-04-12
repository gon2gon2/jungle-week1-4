import sys
input = sys.stdin.readline
N = int(input().rstrip())
mockingbird = [input().rstrip().split() for _ in range(N)]
L = input().rstrip().split()

possible = True

for l in L:
    for m in mockingbird:
        if m and m[0] == l:
            m.pop(0)
            break
    else:
        possible = False
        break
for m in mockingbird:
    if m:possible = False
print("Possible" if possible else "Impossible")


