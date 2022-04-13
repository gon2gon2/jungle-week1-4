# '''
# 큐를 두번 썼고, 동기화가 안 되고 있다.
# 단순히 비어있는 heap에 pop을 하는 것도 카운트해서 return 이 이상해질 수 있다.
# '''
# import heapq
# def solution(operations):
#     answer = []
#     min_heap = []
#     max_heap = []
#     i_cnt = 0 
#     d_cnt = 0
#     for o in operations:
#         cmd = o.split()
#         if cmd[0] == "I":
#             i_cnt += 1
#             heapq.heappush(min_heap, int(cmd[1]))
#             heapq.heappush(max_heap, -int(cmd[1]))
            
#         else:
#             d_cnt += 1
#             if cmd[1] == "-1":
#                 heapq.heappop(min_heap)
#             else:
#                 heapq.heappop(max_heap)
    
#     print(d_cnt)
#     print(i_cnt)
#     return [-max_heap[0], min_heap[0]] if (d_cnt <= i_cnt) and max_heap and min_heap else [0,0]


# 동기화 코드 추가 (remove)
# 36분
import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    i_cnt = 0 
    d_cnt = 0
    for o in operations:
        cmd = o.split()
        if cmd[0] == "I":
            heapq.heappush(min_heap, int(cmd[1]))
            heapq.heappush(max_heap, -int(cmd[1]))
            
        else:
            if cmd[1] == "-1":
                x = heapq.heappop(min_heap)
                max_heap.remove(x)
                heapq.heapify(max_heap)

            else:
                x = heapq.heappop(max_heap)
                min_heap.remove(x)
                heapq.heapify(min_heap)
    
    print(d_cnt)
    print(i_cnt)
    return [-max_heap[0], min_heap[0]] if (d_cnt <= i_cnt) and max_heap and min_heap else [0,0]


