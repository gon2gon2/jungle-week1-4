axis = [
    [0,1],
    [2,3],
]

# def get_axis(r,c):
#     return axis[r//2][c//2]

# print(get_axis(0,1) == 0)
# print(get_axis(1,3) == 1)
# print(get_axis(2,0) == 2)
# print(get_axis(3,3) == 3)

# 기준 4**(N-1) * axis[r//2][c//2] + z_func(r,c,n)


def z_func(n,r,c):
    if n == 1:
        return axis[r][c]

    # 네개의 사분면중 어디에 위치하는 지
    r_for_axis = r//(2**(n-1))
    c_for_axis = c//(2**(n-1))

    # 다음 좌표
    r_prime = r%(2**(n-1))
    c_prime = c%(2**(n-1))

    return 4**(n-1)*axis[r_for_axis][c_for_axis] + z_func(n-1, r_prime, c_prime)


print(z_func(*map(int,input().split())))

# print(z_func(2,3,1)==11)
# print(z_func(3,7,7)==63)