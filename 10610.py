# 30의 배수가 되는 가장 큰 수?
# N을 섞어서 30의 배수가 되게?

# 입력받은 수를 list로 바꾸고 내림차 순 정렬해서 되면 바로 출력-> 틀린 풀이

N = input()
sorted_N = sorted(N, reverse=True)
print(sorted_N)
if sorted_N[-1] == "0" and sum(map(int,sorted_N)) % 3 == 0:
    print("".join(sorted_N))
else:
    print(-1)


# 이딴게 되나?
# 왜 되지. 
# 30 배수의 조건 -> 1의 자리가 0, 전역합이 3의 배수