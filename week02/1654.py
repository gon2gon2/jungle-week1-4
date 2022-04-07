import sys
input = sys.stdin.readline

K, N = map(int, input().split())
Ks = [int(input()) for _ in range(K)]

start, end = 0, max(Ks)


while start <= end:
    length = max((start+end)//2, 1)
    cables = sum([k//length for k in Ks])

    # 많이 나왔다 -> 더 길게 잘라보자 -> start를 올리자
    if cables >= N:
        start = length + 1

    else:
        end = length - 1
print(end)