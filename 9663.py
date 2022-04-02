import copy
N = int(input())
board = [[False] * N for _ in range(N)]

# N=3

# 0이나 max에 닿을 때 까지 +1 +1, -1 -1

def get_diagonal(x,y,n):
    '''x,y의 대각 좌표들을 알려줌'''
    x -= min(x,y)
    y -= min(x,y)

    points = []

    while (x <= n-1) and (y <= n-1):
        points.append((x,y))
        x += 1
        y += 1

    return points


def possible_position(x,y,board):
    if any(board[x]): return False
    elif any([b[y] for b in board]): return False
    elif any([board[x][y] for (x,y) in get_diagonal(x,y,N)]): return False
    return True

set = {}
def n_queen(n, board):
    global cnt
    if n == 0:
        cnt += 1
        return 

    for i in range(N):
        for j in range(N):
            if possible_position(i,j,board):
                temp = copy.deepcopy(board)
                temp[i][j] = True
                n_queen(n-1, temp)



n_queen(N,board)
print()
