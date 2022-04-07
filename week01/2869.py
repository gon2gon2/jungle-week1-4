A,B,V = map(int,input().split())

c = A
day = 1
while c < V:
    c += (A-B)
    day += 1

print(day)