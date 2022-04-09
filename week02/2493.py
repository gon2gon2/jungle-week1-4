
# N = int(input())
# tower_list = list(map(int,input().split()))


# received_tower = [0] * N
# idx_list = [N]
# receiving_idx = N-2
# while receiving_idx >= 0:
#     # print("현재 탑의 높이",tower_list[receiving_idx])

#     # 뒤에서부터 receiving_idx까지 가면서, 현재 타워 높이가 idx의 타워보다 높고, 아직 값이 없으면 값 덮어씌우기
#     for i in range(N-1, receiving_idx, -1):
#         # print(f"현재 순회 범위:{receiving_idx-1} ~ {N-1}")
#         if tower_list[receiving_idx] >= tower_list[i] and not received_tower[i]:
#             received_tower[i] = receiving_idx+1
#     receiving_idx -= 1

# print(received_tower)


# while stack을 하려면 ? 맨 밑에서 pop

N = 5
tower_list = [6, 9, 5, 7, 4]


N = int(input())
tower_list = list(map(int,input().split()))

stack = []
answer = []

# 아하 맨 마지막에 있는 애가 수신탑이구나
for i,v in enumerate(tower_list):
    while stack:
        if stack[-1][1] >= v:
            answer.append(stack[-1][0]+1)
            break
        else:
            stack.pop()

    if not stack:
        answer.append(0)

    stack.append([i,v])

print(answer)


