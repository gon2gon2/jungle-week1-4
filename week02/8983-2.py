import sys
input = sys.stdin.readline

M,N,L = map(int,input().split())
m_list = sorted(map(int, input().split()))
animal_list = [tuple(map(int, input().split())) for _ in range(N)]



# animal 하나씩 꺼내서 가장 가까운 사로를 찾고, 그 사로와의 거리를 재서 ok면 cnt + 1
cnt = 0
for (x, y) in animal_list:
    
    start, end = 0, N-1
    nearest_dist = abs(m_list[0] - x)
    while start <= end:
        # 가장 가까운 사로를 찾아보자
        mid = (start+end) //2
        temp_m = m_list[mid]

        if abs(x-temp_m) < nearest_dist:
            nearest_dist = abs(x-temp_m)

        if x == temp_m:
            nearest_dist = 0
            break

        if temp_m > x:
            end = mid-1
        else:
            start = mid+1

    nearest_dist = min(nearest_dist, abs(x-m_list[end]))
    if nearest_dist+y <= L:
        cnt += 1

print(cnt)

