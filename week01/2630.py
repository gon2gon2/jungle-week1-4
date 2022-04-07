N = int(input()) # 2의 제곱수 2~128
PAPER = [list(map(int, input().split())) for _ in range(N)]

def is_same(x,y,n):
    color = PAPER[x][y]
    # 범위 설정 시작점을 잘못 잡았다
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != PAPER[i][j]:
                return False
    return True
# PAPER = [
#     [1, 1, 0, 0, 0, 0, 1, 1], 
#     [1, 1, 0, 0, 0, 0, 1, 1], 
#     [0, 0, 0, 0, 1, 1, 0, 0], 
#     [0, 0, 0, 0, 1, 1, 0, 0], 
#     [1, 0, 0, 0, 1, 1, 1, 1], 
#     [0, 1, 0, 0, 1, 1, 1, 1], 
#     [0, 0, 1, 1, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1, 1, 1, 1]
# ]
# N = 8
# PAPER = [[1]]
# print(is_same(0,0,1))
# PAPER = [[0]]
# print(is_same(0,0,1))

# print(is_same(2,0,2))

def cut_paper(x,y,n):
    if n == 1:
        color_book[PAPER[x][y]] += 1
        return 

    if is_same(x,y,n):
        # 같으면 그냥 추가하면 됨
        color_book[PAPER[x][y]] += 1
        return


    cut_paper(x,y,n//2)
    cut_paper(x+n//2,y,n//2)
    cut_paper(x,y+n//2,n//2)
    cut_paper(x+n//2,y+n//2,n//2)
    return


color_book = {
    0:0,
    1:0,
}


cut_paper(0,0,N)
print(color_book[0], color_book[1], sep='\n')