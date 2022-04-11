# # 제곱수를 활용해서 K까지를 포함하는 제곱수를 찾은 다음 어떻게 하면 될 거 같은데 잘 모르겠다.

# import sys
# N = int(input())

# numbers = [i*j for i in range(1,N+1) for j in range(1,N+1)]
# sorted_numbers = sorted(numbers)
# print(numbers)
# print(sorted_numbers)
# print(set(sorted_numbers))

# 몇번째 있는 수인지를 알아내는 방법이기 때문에 이전까지의 값보다는 갯수가 중요하다
N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2
    
    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N) # mid 이하의 i의 배수 or 최대 N
    
    if temp >= K: # 이분탐색 실행
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)