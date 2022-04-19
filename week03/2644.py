# 21:25 ~ 21:55 

import sys

input = sys.stdin.readline




# 사람 수
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 촌수를 계산할 사람
target_s, target_e = map(int,input().split())

# 관계의 개수
m = int(input())

# x, y : x는 y의 부모
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(n, people_idx):
    if visited[people_idx]:
        return

    visited[people_idx] = n
    for other_people in graph[people_idx]:
        if not visited[other_people]:
            dfs(n+1, other_people)

dfs(1, target_s)
if visited[target_e]:
    print(visited[target_e] - 1)
else:
    print(-1)
