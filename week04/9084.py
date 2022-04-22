# 시작: 17:08
# 종료: 
# 평가:
import sys

input = sys.stdin.readline

T = int(input())
for t in T:
    N = int(input()) # 동전 가짓수
    coins = [*map(int,input().split())] # 동전들, 오름차순
    M = int(input()) # 만들어야 되는 금액


