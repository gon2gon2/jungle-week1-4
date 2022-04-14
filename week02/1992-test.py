# 배열 대신 인덱스 넣도록 하면 속도 빠를듯
import sys
input = sys.stdin.readline

N = int(input())
PAPER = [input().rstrip() for _ in range(N)]

ans = []


def quad_tree(paper):
    n = len(paper)
    if  n == 1:
        ans.append(paper[0][0])
        return

    cut_idx = n//2
    c = paper[0][0]
    for i in range(n):
        for j in range(n):
            if paper[i][j] != c:
                ans.append('(')
                quad_tree([p[:cut_idx] for p in paper[:cut_idx]])
                quad_tree([p[cut_idx:] for p in paper[:cut_idx]])
                quad_tree([p[:cut_idx] for p in paper[cut_idx:]])
                quad_tree([p[cut_idx:] for p in paper[cut_idx:]])
                ans.append(')')
                return

    ans.append(c)
quad_tree(PAPER)
print(''.join(ans))


