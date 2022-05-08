'''
전에 풀었을 때는 그리디라고 인지하지 못했는데, 다시 풀어보니 그리디가 맞는 것 같다. 
만약 그리디로 안 풀면 for문을 많이 돌면서 직접 회의실을 구현하거나 우선순위 큐를 활용해서 풀 수 있을 것 같다.
'''

import sys
input = sys.stdin.readline

N = int(input())

meeting = [[*map(int, input().split())] for _ in range(N)]
meeting.sort(key = lambda x: (x[1], x[0]))
last = cnt = 0
for s, e in meeting:
    if s >= last:
        cnt += 1
        last = e
print(cnt)
