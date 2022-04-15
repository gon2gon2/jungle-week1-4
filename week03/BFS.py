from collections import deque
number_of_vertex = 9
graph = []
visited = [0] * number_of_vertex
def bfs(graph, s):
    
    visited[s] = True
    dq = deque([s])

    while dq:
        x = dq.popleft()
        visited[x] = True
        print('x', end=' ')

        for p in graph[x]:
            if not visited[x]:
                dq.append(p)


