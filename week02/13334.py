import sys
import heapq
input = sys.stdin.readline

n = int(input())
dots = [sorted(map(int,input().split())) for _ in range(n)]
d = int(input()) #선로의 길이


dots = [[l,r] for [l,r] in dots if r-l<=d] # 가능한 점들만 고른다.
# print("r정렬 전:\t", dots)
dots.sort(key=lambda x: x[1])
# print("r정렬 후:\t", dots) # r이 범위 안에 있다는 게 확실한 거

ans = 0
heap = []


for dot in dots:
    if not heap:
        heapq.heappush(heap, dot)
    else:
        while heap[0][0]+d < dot[1]: # 두점이 다 밖에 있는 경우에는 계속 뺴줘야 되니까!
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap,dot)

    ans = max(ans, len(heap))
print(ans)