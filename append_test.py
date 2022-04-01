import time
lst_1 = [0] * 100000
lst_2 = [0] * 100000
lst_3 = [0] * 100000
ITER_NUM = 10000000

# # append로 추가
# s = time.time()
# for i in range(ITER_NUM):
#     lst_1.append(0)
# e = time.time()
# print(e-s)

# # + operator로 추가
# s = time.time()
# for i in range(ITER_NUM):
#     lst_2+=[0]
# e = time.time()
# print(e-s)


# # extend로 추가
# # mutable의 인자를 
# s = time.time()
# for i in range(ITER_NUM):
#     lst_2.extend([0])
# e = time.time()
# print(e-s)

# 
s = time.time()
for i in range(ITER_NUM):
    lst_2+=[0]
e = time.time()
print(e-s)