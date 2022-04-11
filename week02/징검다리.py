def remove_rocks(rocks, interval, n):
    '''
    rocks : 현재 바위들
    interval: 최소 간격, 이것보다 작으면 remove할 거임
    n: 없앨 바위 수, 이거보다 많이 제거했으면 return False
    '''
    idx = 0
    popped = 0
    temp_rocks = rocks[:]
    while temp_rocks and idx < len(temp_rocks)-1:
        now = temp_rocks[idx]
        right = temp_rocks[idx+1]
        
        if right - now < interval:
            temp_rocks.pop(idx+1)
            popped += 1
            continue
        else:
            idx += 1
            
    # 한두개만 뽑아도 interval을 만족시켜서 더 이상 안 뽑는 경우
    if popped < n:
        for i in range(len(temp_rocks)-1):
            if temp_rocks[i+1] - temp_rocks[i] < interval:
                return popped
        else:
            popped = n
                
    
    
    return popped


def solution(distance, rocks, n):
    '''
    distance: endpoint
    rocks: 바위들의 x 좌표
    n: 뽑을 바위의 개수
    
    '''
    rocks.sort()
    
    answer = 0
    rocks = [0] + rocks + [distance]
    
    start, end = 0, distance
    
    while start <= end:
        mid = (start+end)//2

        popped = remove_rocks(rocks,mid,n)

    
        if popped == n: # 원하는 개수만큼 뽑혔고,
            if answer < mid: # 현재 interval이 기존 interval보다 길어지면 갱신
                answer = mid
    
        # 너무 많이 뽑히면 적게 뽑아야 한다 간격 넓혀
        if popped > n:
            print(f"{popped}개가 뽑혀서 더 좁힙니다.")
            end = mid - 1
        
        # 너무 적거나 같으면 간격 좁혀
        else:
            start = mid + 1
    
    return answer