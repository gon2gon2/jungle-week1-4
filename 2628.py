w, h = map(int,input().split())


cut_w = ['0'] * w
cut_h = ['0'] * h

N = int(input())
for _ in range(N):
    d, p = map(int,input().split())
    if not d :
        cut_h[p] = 1
    else:
        cut_w[p] = 1

max_x = 0
max_y = 0

x_lst = ''.join(map(str,cut_w)).split('1')
for i in range(len(x_lst)-1):
    x_lst[i+1] += '0'

y_lst = ''.join(map(str,cut_h)).split('1')
for i in range(len(y_lst)-1):
    y_lst[i+1] += '0'

mx =len(max(x_lst))
my =len(max(y_lst))
print(mx*my)