# 인풋 -> N명의 [이름, 국, 영, 수]
# 아웃풋 -> 이름 N개

# 조건1: 국어 점수는 내려가게
# 조건2: 조건 1 + 영어 증가
# 조건3: 조건 2 + 수학 감소
# 조건4: 조건 3 + 이름순

# 나의 풀이: 그냥 sort key로 -국,영,-수,이름

import sys
input = sys.stdin.readline

N = int(input())

students = [input().split() for _ in range(N)]
for i in sorted(students, key = lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0])):
    print(i[0])