def install_wifi(arr, interval):
    installed_wifi = 1
    current = arr[0]

    for h in arr[1:]:
        if current + interval <= h:
            # 설치
            installed_wifi += 1
            current = h

    return installed_wifi

import sys
input = sys.stdin.readline

N, C = map(int, (input().split()))
Xs = sorted([int(input()) for _ in range(N)])

start, end = 1, Xs[-1]

while start <= end:
    # 등호 빼야 될 수도
    mid = (start+end)//2  # 거리

    number_of_installed_wifi = install_wifi(Xs,mid)

    if number_of_installed_wifi >= C:
        start = mid + 1

    else:
        end = mid-1

print(end)