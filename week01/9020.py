# # 두 소수의 합으로 나타낼 수 있는 수
# # 짝수 n의 골드바흐 파티션을 구해라
# '''
# n까지의 모든 소수를 구한다.

# 그 안에서 2개씩 뽑아 합쳐 n이 되면 return
# '''
# import sys
# input = sys.stdin.readline

# import math

# prime_numbers = [2]

# def check(n):
#     '''2부터 n의 제곱근까지 가면서 소수인지 판별'''
#     criterio = int(math.sqrt(n))+1
#     idx = 0
#     while prime_numbers[idx] < criterio:
#         if n%prime_numbers[idx] == 0:
#             return False
#         idx +=1
#     prime_numbers.append(n)
#     return True

# from itertools import combinations_with_replacement


# T = int(input())
# ns = [int(input()) for _ in range(T)]
# # sorted_ns = sorted(ns, reverse=True)
# max_n = max(ns)+1
# is_prime = [False] * (max_n)

# for i in range(3,max_n,2):
#     if check(i):
#         is_prime[i] = True


# for n in ns:
#     # n까지 가면서 if is_prime[i]면 리스트에 추가하고 그걸 combination에 넣는다
#     prime_numbers = [i for i in range(3, n+1, 2) if is_prime[i]]
#     prime_partition = [(a,b) for (a,b) in combinations_with_replacement(prime_numbers,2) if a+b == n]
#     print(*sorted(prime_partition, key= lambda x: abs(x[0]-x[1]))[0])






# # 숫자를 받는다
# # 그 숫자보다 작지만 소수인 수를 찾는다
# # 중복 허용 조합으로 2개를 뽑아 합이 n과 일치하는 애들 중 가장 작은 애 pass

# # 최적화 할 수 있을 것 같은 요소: 소수 구하는 과정을 줄인다

# # 검색해서 나온 답이랑 비교
# # 일치하는 것: 소수체크를 한번만 하고 기록해둔다.
# # 다른 것: 나는 bruteforce로 모든 경우를 상정하고 combinations의 첫번쨰부터 돌렸지만, 중앙값부터 돌리면 된다

# # 중앙값부터 왼쪽으로 하나씩, 오른쪽으로 하나씩 간다
# # 왼쪽은 하나만 가고 오른쪽으로 한번만 가는 경우도 있지 않을까?


# T = int(input())
# maxi = 0
# ns = []
# for _ in range(T):
#     x = int(input())
#     if x > maxi:
#         maxi = x


# is_prime = [False] * (maxi+1)
# is_prime[2] = True
# import math

# def check(n):
#     for i in range(3, int(math.sqrt(n)+1)):
#         if :
#             return False
#     return True


# [for i in range(3,maxi+1, 2) if check(i)]
    

# 1. 에라토스테네스의체로 모든 수가 들어있는 리스트를 만든다
# 2. 그 수를 반으로 나눈 부분부터 범위를 넓혀가며 찾는다

# MAX = 10000

# is_prime = [False, False,True] + [True] * MAX

# for i in range(2, MAX):
#     if is_prime[i]:
#         for j in range(i+i, MAX, i):
#             is_prime[j] = False


# T = int(input())
# for _ in range(T):
#     n = int(input()) # 짝수

#     l = n // 2
#     r = l

#     while True:
#         if is_prime[l] and is_prime[r]:
#             print(l,r)
#             break
#         l -= 1
#         r += 1


# 필요한 만큼 까지만 구하는 방식 -> 기존 692ms 에서 288ms로 줄어듬
T = int(input())
ns = [int(input()) for _ in range(T)]

MAX = max(ns)

is_prime = [False, False,True] + [True] * MAX

for i in range(2, MAX):
    if is_prime[i]:
        for j in range(i+i, MAX, i):
            is_prime[j] = False

for n in ns:
    l = n // 2
    r = l

    while True:
        if is_prime[l] and is_prime[r]:
            print(l,r)
            break
        l -= 1
        r += 1
