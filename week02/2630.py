zero = []
one  = []

def check(x):
    if x == 0:
        zero.append('0')
    else:
        one.append('1')
    


def cut_paper(paper):
    length = len(paper)
    base = length//2

    c = paper[0][0]
    for i in range(length):
        for j in range(length):
            if c != paper[i][j]:
                cut_paper([p[:base] for p in paper[:base]])
                cut_paper([p[base:] for p in paper[:base]])
                cut_paper([p[:base] for p in paper[base:]])
                cut_paper([p[base:] for p in paper[base:]])
                return 
    check(c)
    return 

N = int(input())
big_paper = [list(map(int,input().split())) for _ in range(N)]

cut_paper(big_paper)
print(len(zero))
print(len(one))
