# 정렬시킨 후
# 가장 작은 애를 0으로 잡고 그 다음으로 큰 애는 +1

N = int(input())
numbers = list(map(int, input().split()))

number_book = dict()

for i,v in enumerate(sorted(set(numbers))):
    number_book[v] = i

for i in range(N):
    numbers[i] = number_book[numbers[i]]

print(*numbers)