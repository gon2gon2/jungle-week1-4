



N = 8
PAPER = [
[1, 1, 0, 0, 0, 0, 1, 1], 
[1, 1, 0, 0, 0, 0, 1, 1], 
[0, 0, 0, 0, 1, 1, 0, 0], 
[0, 0, 0, 0, 1, 1, 0, 0], 
[1, 0, 0, 0, 1, 1, 1, 1], 
[0, 1, 0, 0, 1, 1, 1, 1], 
[0, 0, 1, 1, 1, 1, 1, 1], 
[0, 0, 1, 1, 1, 1, 1, 1]
]
# PAPER = [
#     [0,0],
#     [1,0]
# ]
# base = len(PAPER)//2
# print([p[:base]for p in PAPER[:base]][0][0])
# print([p[:base]for p in PAPER[base:]][0][0])
# print([p[base:]for p in PAPER[:base]][0][0])
# print([p[base:]for p in PAPER[base:]][0][0])

import sys
input = sys.stdin.readline

N = int(input())
PAPER = [list(map(int,input().split())) for _ in range(N)]

zero = []
one = []


def divide_and_conquer(paper):
    n = len(paper)
    base = n//2

    c = paper[0][0]

    for i in range(n):
        for j in range(n):
            if paper[i][j] != c:
                divide_and_conquer([p[:base]for p in paper[:base]])
                divide_and_conquer([p[:base]for p in paper[base:]])
                divide_and_conquer([p[base:]for p in paper[:base]])
                divide_and_conquer([p[base:]for p in paper[base:]])
                return
    if c == 1:
        one.append('1')
    else:
        zero.append('0')

divide_and_conquer(PAPER)
print(len(zero))
print(len(one))