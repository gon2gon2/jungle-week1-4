import sys
input = sys.stdin.readline
D = 1000


N, B = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

def mutiply_matrix(A,B):
    ''' matrix 두개 받아서 곱한 뒤 반환'''
    s = len(A)
    temp_A = [[0]*s for _ in range(s)]

    for i in range(s):
        for j in range(s):
            # # 원소 구하기 1 -> 굿
            # elem = 0
            # for k in range(s):
            #     elem += A[i][k] * B[k][j]
            # temp_A[i][j] = elem%D

            # 원소 구하기 2 -> 별로같음
            row = A[i]
            col = [b[j] for b in B]
            v = sum([r*c for r,c in zip(row,col)])
            temp_A[i][j] = v%D
    return temp_A


def get_square(A, n):
    if n == 1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] %= D
        return A
    
    # 한번만 구해서 함수에 넣어줘야 시간 초과 X
    temp = get_square(A, n//2)

    if n % 2 == 1: # 홀수다
        return mutiply_matrix(mutiply_matrix(temp, temp), A)

    else:
        return mutiply_matrix(temp, temp)


new_A = get_square(A, B)
for r in new_A:
    print(*r)