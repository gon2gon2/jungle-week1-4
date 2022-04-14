# append를 먼저 해주면 나중에 합쳐진 문자열에 대해 체크할 필요 없다

input_string = input().rstrip()
ex_string = input().rstrip()

input_length = len(input_string)
ex_length = len(ex_string)
stack = []

for i in range(input_length):
    stack.append(input_string[i])
    while len(stack) >= ex_length and ''.join(stack[-ex_length:]) == ex_string:
        for _ in range(ex_length):
            stack.pop()

print(''.join(stack) if stack else "FRULA")