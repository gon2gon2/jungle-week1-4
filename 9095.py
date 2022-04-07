def make_number(n):
        if n == N:
            return 1
        if n > N:
            return 0

        return make_number(n+1) + make_number(n+2) + make_number(n+3)

T = int(input())
for _ in range(T):
    N = int(input())
    print(make_number(0))