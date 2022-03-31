number_book = {i:0 for i in range(10)}

A = int(input())
B = int(input())
C = int(input())

for i in str(A*B*C):
    number_book[int(i)] += 1

for k,v in number_book.items():
    print(v)