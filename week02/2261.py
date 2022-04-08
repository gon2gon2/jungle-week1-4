import sys
input = sys.stdin.readline

N = int(input())
dots = sorted(
    [tuple(map(int, input().split())) for _ in range(N)],
    key=lambda x: x[0]
    )

def get_distance(dot_1, dot_2):
    return (dot_1[0] - dot_2[0])**2 + (dot_1[1] - dot_2[1])**2

def divide_and_conquer(l_idx, r_idx):

    if l_idx == r_idx:
        return sys.maxsize

    # if n == 2:
    #     return get_distance(dots[0], dots[1])

    m = (l_idx + r_idx) // 2 #중앙값의 인덱스
    min_dist = min(divide_and_conquer(l_idx,m), divide_and_conquer(m+1,r_idx))
    potential_dots = []


    # min_dist보다 같아도 break인 이유: 같으면 잘해봐야 min_dist라서 굳이 할 필요 X
    for i in range(m, l_idx-1, -1):
        if (dots[i][0] - dots[m][0]) ** 2 >= min_dist:
            break
        else:
            potential_dots.append(dots[i])

    for j in range(m+1, r_idx+1):
        if (dots[j][0] - dots[m][0]) ** 2 >= min_dist:
            break
        else:
            potential_dots.append(dots[j])


    potential_dots = sorted(potential_dots, key=lambda x: x[1])

    for i in range(len(potential_dots)-1):
        for j in range(i+1, len(potential_dots)):
            if (potential_dots[i][1] - potential_dots[j][1]) ** 2 < min_dist:
                dist = get_distance(potential_dots[i], potential_dots[j])
                min_dist = min(dist, min_dist)

            else:
                break
    
    return min_dist

mini = divide_and_conquer(0, len(dots)-1)
print(mini)
