numbers = [int(input()) for _ in range(9)]

idx, x = 0, 0
for i,n in enumerate(numbers):
    if n > x:
        idx = i+1
        x = n
print(x)
print(idx)