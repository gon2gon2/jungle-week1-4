# A, B, C = 10,11,12

# power = [1] * (B+1)
A ,B, C =map(int,input().split())

def n_square(x, n, d):
    if n==0:
        return 1
    elif n == 1:
        return x%d

    temp = n_square(x, n//2, d)

    if n % 2 == 0:
        return (temp*temp)%d

    else:
        return (temp*temp*x)%d

print(n_square(A ,B, C))
