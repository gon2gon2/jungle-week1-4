# 28분 소요 -> 80%쯤에서 틀렸습니다 -> 수정할수록 이상해져서 나중에 다시 -> sort가 문제였나보다 ㅂㄷㅂㄷ
from collections import deque
import sys
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
ans = []
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

queue = deque([X])
visited = [-1] * (N+1)
visited[X] = 0
while queue:
    now = queue.popleft()

    for i in graph[now]:
        if visited[i] == -1:
            visited[i] = visited[now]+1
            queue.append(i)
            if visited[i] == K:
                ans.append(i)

if not ans:
    print(-1)
else:

    ans.sort()
    for a in ans:
        print(a)