# N, K = map(int, input().split())
# req_num = N-K
# number = list(map(int,list(input())))
# # print(number)

# stack = []
# for i in range(N):
#     # 더이상 거르면 안 되는 경우 -> break
#     if len(stack) + (N-i) == K: 
#         # print("1더이상 거를 수 없음->출력")
#         break

#     # print("index:", i, "stack:", stack)

#     while stack and len(stack) + (N-i) > req_num:

#         if stack[-1] < number[i]:
#             stack.pop()
#             continue

#         else:
#             stack.append(number[i])
#             break

#     if len(stack) + (N-i) == req_num:
#         stack += number[i:]
#         break

#     if not stack:
#         stack.append(number[i])

# print("".join(list(map(str,stack[:req_num]))))


#########################1시간 걸림########################



N, K = map(int, input().split())
number = list(input())
k, stack = K, []

for i in range(N):
    while k > 0 and stack and stack[-1] < number[i]:
        stack.pop()
        k -= 1
    stack.append(number[i])

print("".join(stack[:N-K]))

