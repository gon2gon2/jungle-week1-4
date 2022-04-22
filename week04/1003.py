# 시작:
# 종료:
# 평가: 접근법이 기억나서 쉽게 풀었다
import sys

input = sys.stdin.readline


zero = [1,0,1]
one = [0,1,1]

T = int(input())

for t in range(T):
    N = int(input())

    for i in range(3, N+1):
        zero.append(zero[-1] + zero[-2])
        one.append(one[-1] + one[-2])

    print(zero[N],one[N])
        
