N, S = map(int,input().split())
numbers = list(map(int, input().split()))
ans = [0]
def get_combination(i,s):
    if i == N:
        if s == S:
            ans[0] += 1
        return

    get_combination(i+1, s+numbers[i])
    get_combination(i+1, s)

get_combination(0,0)
print(ans[0]) if S else print(ans[0]-1)