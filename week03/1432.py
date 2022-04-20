# 시작: 23:06
# 종료:
# 평가:
import sys
import heapq
input = sys.stdin.readline


N = int(input())

graph = [[] for _ in range(N+1)]
in_degree = [[False] * (N+1) for _ in range(N+1)]
answer = [0] * (N+1)
heap = []


for i in range(1, N+1):
    row = [*map(int,list(input().strip()))]
    for j in range(1,N+1):
        if row[j-1] == 1:
            graph[i].append(j)
            in_degree[i][j] += 1

for i in in_degree:
    print(i)
for i in range(1,N+1):
    if in_degree[i] == 0:
        heapq.heappush(heap, i)
print(in_degree)
print("최초 힙:", heap)
cnt = 1
while heap:

    now = heapq.heappop(heap)
    answer[now] = cnt
    for next_node in graph[now]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            heapq.heappush(heap, next_node)
    print("힙:", heap)
    cnt += 1
if min(answer[1:]) == 0:
    print(-1)
else:
    print(*answer[1:])


