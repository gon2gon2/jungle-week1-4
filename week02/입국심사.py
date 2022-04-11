# 나의 실수: shortest는 최소 시간이라 temp(사람 수)랑 비교하는 게 아니라 mid(시간)랑 비교해야 한다.


def solution(n, times):
    start = 0
    end = max(times)*n
    shortest = end
    while start <= end:
        mid = (start+end)//2
        
        temp = 0
        for time in times:
            temp += mid//time
            
        if temp >= n and mid < shortest: # 여기서 틀렸었다.
            shortest = mid
        
        if temp >= n:
            end = mid-1
        else:
            start = mid+1
            
    return shortest