# # 방법 1
# n = int(input())
# prime_numbers = []
# for i in range(2,n):
# 	if n % i == 0:
# 		prime_numbers.append(i)


# # 방법 2
# n = int(input())
# prime_numbers = [2]
# for i in range(3, n+1, 2):
#     for p in prime_numbers:
#         if i%p == 0:
#             prime_numbers.append(i)



# 소수의 제곱이 n보다 커지기 전까지,
#   소수로 하나씩 나눠본다
#   만약 나뉘면 break,
# while 끝날 때 까지 안 나뉘면 소수 추가


# T = int(input())
# maxi = 0
# ns = []
# for _ in range(T):
#     x = int(input())
#     if x > maxi:
#         maxi = x




# prime_numbers = [2,3]
# n = 1000
# for n in range(5, n+1, 2):
#     idx = 1
#     while prime_numbers[idx] ** 2 < n:
#         if n % prime_numbers[idx] == 0:
#             break
#         idx += 1
#     else:
#         prime_numbers.append(n)


# for n in ns:
#     for p in prime_numbers:
#         if p ** 2 > n:
            



## 어쩌구의 체
n = 10000
is_prime = [False, False] + [True] * n

for i in range(2,10001,2):
    if is_prime[i]:
        for j in range(i*2, 10001, i):
            is_prime[j] = False

for i in range(100):
    if is_prime[i]:
        print(i)






















    # while prime_numbers[idx] ** 2 < n:
        
    #     if n % prime_numbers[idx]:
    #         break
    #     idx += 1
    # else:



