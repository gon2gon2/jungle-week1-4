from sys import stdin
input = stdin.readline

N, C = map(int, input().split())
# 인접한 공유기 사이의 거리를 최대
position = sorted([int(input()) for _ in range(N)])


