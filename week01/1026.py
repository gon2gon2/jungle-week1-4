# 1026번


# # B는 정렬하면 안 된다!
# N = int(input())
# A = sorted(map(int, input().split()), reverse=True)
# B = sorted(map(int, input().split()), reverse=False)

# # 합이 최소
# # -면 가장 큰애랑 곱해주고 -> 다 양수라서 ㄱㅊ
# # 간단 생각: A는 크게 ,B는 작게 정렬 후 곱해줘서 더하기


# s = 0
# for a, b in zip(A,B):
#     s += a*b

# print(s)
N = int(input())
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()))
s = 0
for a in A:
    b = min(B)
    B.remove(b)
    s += a*b
print(s)
