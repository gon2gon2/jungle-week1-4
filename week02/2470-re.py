# 틀린 이유: left<right에 =가 들어가서.
# 등호가 들어가면 둘이 같은 애를 고를 수도 있기 때문에 그런듯.

N = int(input())
fluids = sorted(map(int, input().split()))
TARGET = 0
left, right = 0, N-1


best = [fluids[0], fluids[-1]]
while left < right:
    value = fluids[left] + fluids[right]
    if abs(value) <= abs(sum(best)):
        best = [fluids[left], fluids[right]]

    if value > TARGET:
        right -= 1
        
    elif value < TARGET:
        left += 1

    else:
        break

print(*best)
'''


5
-2 4 -99 -1 98


'''