import sys
input = sys.stdin.readline

N = int(input())
ns = [0] * 10001

for _ in range(N):
    n = int(input())
    ns[n] += 1

for i in range(10001):
    if ns[i]:
        for _ in range(ns[i]):
            print(i)