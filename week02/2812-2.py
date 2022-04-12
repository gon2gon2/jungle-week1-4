# 24분

N, K = map(int,input().split())
number = list(map(int,list(input())))
length = N-K
k = K
stack = []

for i in range(len(number)):
    while k and stack and len(stack)+len(number) -i > length and stack[-1] < number[i]:
        # 쓸데없이 pop 제한을 2번이나 걸었음(k, len(stack)~~)
        stack.pop()
        k -= 1
    stack.append(number[i])

if len(stack) > length:
    stack = stack[:length]

print(''.join(list(map(str, stack))))