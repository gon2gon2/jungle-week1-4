# 한 번호가 다른 번호의 접두어인 경우가 없어야 한다
# 나의 접근 : 완전 탐색
# 풀이 : sort를 하면 prefix로 정렬이 되므로 

# 오름차순 정렬 후 N, n-1회 정렬


# def check_number(N, number_list):
#     # 이중for
#     for i in range(N-1):
#         for j in range(i+1, N, 1):
#             if number_list[j].startswith(number_list[i]):
#                 return "NO"
#     return "YES"


import sys
input = sys.stdin.readline

def check_number_prefix(n,number_list):
    # print("number_list:", number_list)
    number_list = sorted(number_list)
    for i in range(n-1):
        # print(i)
        # print(f"{number_list[i+1]}가 {number_list[i]}로 시작하나")
        if number_list[i+1].startswith(number_list[i]):
            return "NO"
    return "YES"


T = int(input())

for t in range(T):
    N = int(input())
    numbers = [input().rstrip() for i in range(N)]
    print(check_number_prefix(N,numbers))