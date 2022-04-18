import sys
from collections import deque

input = sys.stdin.readline

# N은 최종제품, 1~N-1은 기본, 중간부품
N = int(input())

# 부품 조합
M = int(input())

number_of_components = [[0] * (N + 1) for _ in range(N + 1)]
need = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)
q = deque()
for _ in range(M):
    X, Y, K = map(int, input().split())
    need[Y].append((X, K))
    degree[X] += 1

for i in range(1, N + 1):
    if not degree[i]:
        q.append(i)

while q:
    current_part = q.popleft()

    for middle_idx, middle_val in need[current_part]:
        # 기본 부품인 경우
        if not max(number_of_components[current_part]):
            number_of_components[middle_idx][current_part] = middle_val

        # 중간 부품인 경우
        else:
            for i in range(1, N + 1):
                number_of_components[middle_idx][i] += (
                    middle_val * number_of_components[current_part][i]
                )
        degree[middle_idx] -= 1
        if degree[middle_idx] == 0:
            q.append(middle_idx)

for i in range(1, N + 1):
    if number_of_components[-1][i] > 0:
        print(i, number_of_components[-1][i])
