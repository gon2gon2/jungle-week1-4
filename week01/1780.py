# pypy 는 1100
# python3 은 3800


N = int(input()) # 3의 n제곱
paper = [list(map(int,input().rstrip().split())) for _ in range(N)]
answer = []

def cut_paper(x,y,n):
    if n == 1:
        answer.append(paper[x][y])
        return

    color = paper[x][y]

    for i in range(x,x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                cut_paper(x,y,n//3)
                cut_paper(x+n//3,y,n//3)
                cut_paper(x+n//3+n//3,y,n//3)
                
                cut_paper(x,y+n//3,n//3)
                cut_paper(x+n//3,y+n//3,n//3)
                cut_paper(x+n//3+n//3,y+n//3,n//3)

                cut_paper(x,y+n//3+n//3,n//3)
                cut_paper(x+n//3,y+n//3+n//3,n//3)
                cut_paper(x+n//3+n//3,y+n//3+n//3,n//3)

                return
    answer.append(color)
    return 
cut_paper(0,0,N)
zero=p1=n1 = 0

for p in answer:
    if p == 0:
        zero += 1
    elif p == 1:
        p1 += 1
    elif p == -1:
        n1 += 1

print(n1)
print(zero)
print(p1)