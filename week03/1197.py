# 총 소요시간 22분
# 크루스칼 알고리즘, union-find 구현
import sys
input = sys.stdin.readline
V, E = map(int,input().split())
edge = []
cycle = {i:i for i in range(1,V+1)}
for _ in range(E):
    edge.append([*map(int,input().split())])
edge = sorted(edge, key=lambda x:x[2])


def find_parent(x):
    if cycle[x] == x:
        return x
    return find_parent(cycle[x])

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        cycle[y] = x
        return 
    cycle[x] = y
    return 

def find_union(x,y):
    return find_parent(x) == find_parent(y)

w = 0
for i in range(E):
    e = edge[i]
    if not find_union(e[0], e[1]):
        union_parent(e[0], e[1])
        w += e[2]
        # 꼭 필요한 건 아닌데 속도를 개선하기 위해선 현재 연결된 edge 수가 n-1이 되면 break해서 더 빨리 끝낼 수도 있을 것 같다.
print(w)





# print(find_parent(1))
# print(find_parent(2))
# print(find_parent(3))
# print(find_parent(4))
# print(find_parent(5))
# union_parent(1,4)
# union_parent(4,5)
# print()
# print(find_parent(1))
# print(find_parent(2))
# print(find_parent(3))
# print(find_parent(4))
# print(find_parent(5))
# print()
# print(find_union(1,4))
# print(find_union(1,3))
# print(find_union(4,5))
