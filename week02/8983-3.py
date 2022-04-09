import sys
input = sys.stdin.readline
M,N,L = map(int, input().split())
m_list = sorted(map(int,input().split()))
animal_list = [tuple(map(int,input().split())) for _ in range(N)]

cnt = 0

for animal in animal_list:
    start,end = 0, M-1
    best = sys.maxsize
    if animal[1] > L:
        continue
    while start <= end:
        mid = (start+end)//2
        # 거리를 측정
        distance = m_list[mid] - animal[0]

        if abs(distance) < best:
            best = abs(distance)

        if distance < 0:
            start = mid+1
        else:
            end = mid-1

    if best + animal[1] <= L:
        cnt += 1
print(cnt)