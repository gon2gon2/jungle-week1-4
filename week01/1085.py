# 백준: 1085번
'''
h               w,h


0,0             w


x: 6 -> 10 or 0 -> 10으로 4만큼 이동
y: 2 -> 3 or 0 -> 3으로 1만큼 이동

끝좌표가 아니라 x나 y 둘 중 하나만 가도 된다
'''


x, y, w, h = map(int, input().split())
def answer(x,y,w,h):
    return min(x, y, w-x, h-y)
print(answer(x,y,w,h))

# print(answer(6,2,10,3) == 1)
# print(answer(1,1,5,5) == 1)
# print(answer(653,375,1000,1000) ==347)
# print(answer(161,181,762,375) == 161)

# print(answer(6,2,10,3))
# print(answer(1,1,5,5))
# print(answer(653,375,1000,1000))
# print(answer(161,181,762,375))

