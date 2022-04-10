# ##### 정답은 나오지만 시간초과

# import heapq
# import sys
# input = sys.stdin.readline

# N, K = map(int,input().split())

# jewerly = [list(map(int,input().split())) for _ in range(N)]
# jewerly.sort(key=lambda x:x[1], reverse=True)

# bag = [int(input()) for _ in range(K)]
# heapq.heapify(bag)


# ans = 0
# for j in jewerly:
#     temp = []

#     while bag:
#         # bag에 담기면 끝냄
#         pop = heapq.heappop(bag)
#         if pop >= j[0]:
#             ans += j[1]
#             break
#         # 안 담기면
#         temp.append(pop)
#     bag += temp
# print(ans)



###### 
# 각 가방마다 담을 수 있는 모든 보석을 최소힙으로 찾는다
# 그 안에서 가장 비싼 보석을 찾는다
# 내 코드는 for문이 잘못됐다. 가방을 먼저 기준으로 했어야 됐다.

import heapq
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

jewerly = []
for _ in range(N):
    heapq.heappush(jewerly, tuple(map(int,input().split())))

bag = [int(input()) for _ in range(K)]
bag.sort()


answer = 0
temp = []    # 
for b in bag:
    while jewerly and jewerly[0][0] <= b:
        heapq.heappush(temp, -heapq.heappop(jewerly)[1])
    if temp: # 가방에 들어갈 보석이 있다
        answer -= heapq.heappop(temp)
    elif not jewerly:
        break
print(answer)