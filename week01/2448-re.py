# 3 * 2**k / 3곱하기 2의제곱수


N = int(input())
graph = [[' '] * 2 * N for _ in range(N)]


first_stars = ["*","* *","*****"]

def countin_star(x,y,n):
    if n == 3:
        graph[y][x] = "*"
        graph[y+1][x-1]=graph[y+1][x+1] = "*"
        for i in range(-2,3):
            graph[y+2][x+i] = '*'
        
        return
    nn = n//2
    countin_star(x,y,n//2)
    countin_star(x-nn,y+nn,nn)
    countin_star(x+nn,y+nn,nn)
    

countin_star(N-1,0,N)
for g in graph:
    print(''.join(g))




# def counting_star(n,input_star):
#     output_star = []
#     if n//3 == 1:
#         return input_star

#     for input_s in input_star:
#         output_star.append(input_s)
#     # i가 n//2를 넘어가면
#     for i, input_s in enumerate(input_star):

#         if i % 3 == 0:
#             output_star.append(input_s + " "*(5)*(N//n) + input_s)
#         elif i % 3 == 1:
#             output_star.append(input_s + " "*(3)*(N//n) + input_s)
#         elif i % 3 == 2:
#             output_star.append(input_s + " "*(1)*(N//n) + input_s)


#     return counting_star(n//2, output_star)
        


# stars = counting_star(N,first_stars)

# print(stars)
# for s in stars:
#     print(f"{s:^47}")

