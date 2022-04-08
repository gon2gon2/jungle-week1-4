# 1. 점들을 받는다
# 2. left right을 나눠서 min_dist를 구한다
# 3. x값 기준으로 min_dist후보가 아닌 애들은 거르고 모은다
# 4. y값으로 정렬한 다음 길이 재서 min찾는다

import sys
input = sys.stdin.readline

N = int(input())
sorted_dots = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])

def get_dist(dot_1, dot_2):
    return (dot_1[0] - dot_2[0])**2 + (dot_1[1] - dot_2[1])**2

def dnc(l_idx, r_idx):
    if l_idx == r_idx:
        return sys.maxsize

    mid = (l_idx + r_idx)//2

    nearest_left = dnc(l_idx, mid)
    nearest_right = dnc(mid+1, r_idx)

    nearest_dist = min(nearest_left, nearest_right)

    potential_dots = []

    for i in range(mid,l_idx-1,-1): # l_idx-1은 뭐지 # 끝까지 안 가니까 인듯
        if (sorted_dots[i][0] - sorted_dots[mid][0]) ** 2 >= nearest_dist:
            break
        else:
            potential_dots.append(sorted_dots[i])

    for j in range(mid+1, r_idx+1): # r_idx+1은 머냐
        if (sorted_dots[j][0] - sorted_dots[mid][0]) ** 2 >= nearest_dist:
            break
        else:
            potential_dots.append(sorted_dots[j])

    potential_dots.sort(key=lambda x:x[1])

    for i in range(len(potential_dots)-1):
        for j in range(i+1, len(potential_dots)):
            if (potential_dots[i][1] - potential_dots[j][1]) ** 2 < nearest_dist:
                dist = get_dist(potential_dots[i], potential_dots[j])
                nearest_dist = min(dist,nearest_dist)
            else:
                break

    return nearest_dist


dist = dnc(0,N-1)
print(dist)