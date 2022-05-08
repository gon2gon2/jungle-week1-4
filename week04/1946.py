# 시작: 20:20
# 종료: 21:20

'''
2중 for를 사용하면 답은 나오겠지만 당연히 시간 초과가 발생할 것이다.
정렬을 이용하면 일단 [0]인덱스에서는 앞서있기 때문에(게다가 중복도 없다), [1]만 확인하면 되는 것이다.
'''

import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    
    N = int(input())

    employee = [[*map(int, input().split())] for _ in range(N)]
    employee.sort()
    best = employee[0][1]
    cnt = 1
    for i in range(1, N):
        if best > employee[i][1]:
            cnt += 1
            best = employee[i][1]

    print(cnt)

