A,B,C = 10,11,12

A,B,C = map(int, input().split())

def n_square(a,b,c):
    if b == 0:
        return 1
    elif b == 1:
        return a%c

    temp = n_square(a,b//2,c)
    if b%2:
        return (temp * temp * a)%c

    return (temp * temp)%c

print(n_square(A,B,C))
