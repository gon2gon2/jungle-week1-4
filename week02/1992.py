
# N = 8
# VIDEO = [
#     [1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 0, 0, 0, 0],
#     [0, 0, 0, 1, 1, 1, 0, 0],
#     [0, 0, 0, 1, 1, 1, 0, 0],
#     [1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 0, 0, 1, 1],
#     [1, 1, 1, 1, 0, 0, 1, 1]
#     ]

# N = 4
# VIDEO = [
#     [1,1,1,1],
#     [1,1,1,1],
#     [0,0,0,1],
#     [0,0,0,1],
# ]

# N = 2
# VIDEO = [
#     [0,1],
#     [0,1],
# ]

import sys
input = sys.stdin.readline
tree = []


N = int(input())
VIDEO = [list(input()) for _ in range(N)]

def dnq(input_video):
    n = len(input_video)

    if n == 1:
        tree.append(input_video[0][0])
        return 

    base = n//2
    

    first = input_video[0][0]
    for i in range(n):
        for j in range(n):
            if input_video[i][j] != first:
                tree.append('(')
                dnq([v[:base] for v in input_video[:base]])
                dnq([v[base:] for v in input_video[:base]])
                dnq([v[:base] for v in input_video[base:]])
                dnq([v[base:] for v in input_video[base:]])
                tree.append(')')
                return
    tree.append(f'{first}')

dnq(VIDEO)
print("".join(tree))