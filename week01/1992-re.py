

N = 8

video = [
    list('00000000'),
    list('00000000'),
    list('00001111'),
    list('00001111'),
    list('00011111'),
    list('00111111'),
    list('00111111'),
    list('00111111'),
]
''' string으로 쭉 늘여놓고 해보기 앞에서부터 계속 붙는 식이라 append가 맞았다'''
# def quad_tree(n, input_tree):
#     if n//2 == 1:
#         print(n)
#         return input_tree

#     return [x[:n//2] for x in input_tree[:n//2]]
    # if n == 1:
    #     return input_tree


    # return quad_tree(n//2,''.join([input_tree[0],input_tree[1],input_tree[2],input_tree[3]]))


print(video)

# N = int(input())
# video = [list(input()) for _ in range(N)]
# print(video)


def quad_tree(x,y,n):
    color = video[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != video[i][j]:
                # 쪼개서 다시 함수 수행
                answer.append("(")
                quad_tree(x,y,n//2)
                quad_tree(x,y+n//2,n//2)
                quad_tree(x+n//2,y,n//2)
                quad_tree(x+n//2,y+n//2,n//2)
                answer.append(")")
                return
    answer.append(color)
answer = []

n = 8
quad_tree(0,0,n)
print("".join(map(str,answer)))
