# import copy

N = int(input())
N = 8
# board = [[False] * N for _ in range(N)]

# N=3

# 0이나 max에 닿을 때 까지 +1 +1, -1 -1
# 나중에 중복체크 할때 이중리스트를 set에 넣긴 메모리가 너무 많이 드니 파싱해서 리스트나 문자열로 만들어서 appned


# def get_diagonal(x,y,n):
#     '''x,y의 대각 좌표들을 알려줌'''
#     x -= min(x,y)
#     y -= min(x,y)

#     points = []

#     while (x <= n-1) and (y <= n-1):
#         points.append((x,y))
#         x += 1
#         y += 1

#     return points



# def possible_position(x,y):
#     if (not check_set[x]
#         and not check_dia_1[x+y]
#         and not check_dia_2[x-y+N-1]) : return True
#     return False

# print(f"N={N}")
# print(f"((2*N)-1)={((2*N)-1)}")
N = int(input())

position = [0] * N
check_set = [False] * N
check_dia_1 = [False] * ((2*N)-1)
check_dia_2 = [False] * ((2*N)-1)


def put():
    global cnt
    # print(position)
    cnt += 1

cnt = 0
def n_queen(i):
    for j in range(N):
        if (not check_set[j]
            and not check_dia_1[i+j]
            and not check_dia_2[i-j+N-1]) :
            position[i] = j
            if i+1 == N:
                put()

            else: 
                check_set[j] = check_dia_1[i+j] = check_dia_2[i-j+N-1] = True
                n_queen(i+1)
                check_set[j] = check_dia_1[i+j] = check_dia_2[i-j+N-1] = False

n_queen(0)
print(cnt)
# for b in board_lst:
#     for o in b:
#         print(o)
#     print()


# n = int(input())

# position = [0] * n
# check_1 = [False] * n
# check_2 = [False] * (n*2 - 1)
# check_3 = [False] * (n*2 - 1)


# def set_queen(i):
#     global cnt
#     for j in range(n):
#         if (
#             not check_1[j]
#             and not check_2[i+j]
#             and not check_3[j-i+n-1]
#         ):
#             position[i] = j
#             if i == n:
#                 cnt+=1
#             else:
#                 check_1[j] = check_2[i+j] = check_3[j-i+n-1] = True
#                 set_queen(i+1)
#                 check_1[j] = check_2[i+j] = check_3[j-i+n-1] = False
#                 print(position)

# cnt = 0
# set_queen(0)
# print(cnt)