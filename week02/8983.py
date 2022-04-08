import sys
input = sys.stdin.readline

M,N,L = map(int,input().split())
M_list = sorted(map(int, input().split()))
animal_list = [tuple(map(int,input().split())) for _ in range(N)]


def find_nearest_m(target_x:int,m_list:list, number_of_m:int):
    start, end = 0, number_of_m-1
    nearest = end # 가장 가까웠던 인덱스
    # 부등호를 빼고 마지막에 걸친 값, 걸친값-1로 거리체크
    while start <= end:
        mid = (start+end)//2
        current_x = m_list[mid]

        if current_x == target_x:
            return m_list[mid]

        if abs(current_x - target_x) < abs(m_list[nearest] - target_x):
            nearest = mid

        elif current_x < target_x:
            start = mid +1

        else:
            end = mid - 1
    return m_list[nearest]

cnt = 0

for a in animal_list:
    nearest_m = find_nearest_m(a[0],M_list,M)
    distance = abs(nearest_m-a[0]) + a[1]

    if distance <= L:
        cnt += 1

print(cnt)

# # 가장 가까운 사로 찾기 함수 테스트
# print(find_nearest_m(1,M_List, M)==1) 
# print(find_nearest_m(2,M_List, M)==1) 
# print(find_nearest_m(3,M_List, M)==4) 
# print(find_nearest_m(5,M_List, M)==4) 
# print(find_nearest_m(7,M_List, M)==6) 
# print(find_nearest_m(9,M_List, M)==9)
