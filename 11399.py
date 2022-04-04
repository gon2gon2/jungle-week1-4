def atm(N, array):
    total_time = 0

    array = sorted(array)
    
    for i in range(N):
        total_time += sum(array[:i]) + array[i]

    return total_time

N = int(input())
array = list(map(int,input().split()))

print(atm(N, array))