def calc(x):
    if x == 0:
        return 0
    return x + calc(x-1)

def answer(x):
    s = 0
    for i in x.split('X'):
        if i :
            s += calc(len(i))
    return s



T = int(input())
for _ in range(T):
    print(answer(input()))