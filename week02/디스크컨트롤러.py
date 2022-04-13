'''
레퍼런스를 한번 보고 구현했는데도 어려웠다
우선순위큐 쉽지 않다.
매순간의 판단을 힙에서 꺼내기만 하면 됐다.
완벽한 결과가 나오게 하려고 하지 말고 매순간 판단하게 하는 구현으로 먼저 짜보자
'''
import heapq
def solution(jobs):
    answer = 0
    # 현재 완료한 작업 개수 / 시작시점 / 현재 시간
    idx,start,now = 0,-1,0
    heap = []
    
    while idx < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, job[::-1])
        if heap:
            current_job = heapq.heappop(heap)
            # 시작시간을 현재로 맞춰주고
            start = now 
            # heap에는 현재 가능한 일만 넣어놔서 무조건 현재가 크거나 같다
            now += current_job[0]
            answer += (now - current_job[1])
            # 작업 완료 처리
            idx += 1
        else:
            now += 1
    return answer // len(jobs)