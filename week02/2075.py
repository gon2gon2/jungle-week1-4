'''
후보 1 : N만큼의 리스트 생성 후 순회하면서 앞 머리만 찾은 다음 count하면서 pop
후보 2: 리스트 하나에 매 인풋을 heappush(N번) and heappop(1번)
1번은 누가 봐도 메모리초과인데 2번도 메모리초과

'''

# 메모리초과
# import heapq
# N = int(input())
# heap = []
# cnt = 0
# for _ in range(N):
#     for i in list(map(int,input().split())):
#         heapq.heappush(heap, i)
#     heapq.heappop(heap)
#     cnt += 1

# while cnt:
#     x = heapq.heappop(heap)
#     cnt -=1
# print(x)

'''
heapq를 쓰면 최솟값이 항상 정리되어 있다.
최솟값보다 큰 값일 들어왔을 때만 새로 넣어주면 작은애들은 다 빠질 것이다.

'''

import heapq
N = int(input())
heap = [] # 가장 작은 값이 맨 위에 있다(필요없는 값)
cnt = 0
for _ in range(N):
    numbers = list(map(int,input().split()))

    if not heap:
        for num in numbers:
            heapq.heappush(heap, num)
    
    else:
        for num in numbers:
            if heap[0] < num: # 우리가 원하는 건 큰 값이니 틈날 떄 마다 작은 값 제거
                heapq.heappush(heap, num)
                heapq.heappop(heap)
            # 현재까지 나온 값들 중 상위 N개로 유지된다.
print(heap[0])
