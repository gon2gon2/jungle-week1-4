# 소요시간 9분
import sys
input = sys.stdin.readline
router_buffer = []

buffersize = int(input())
now_size = 0
while True:
    x = int(input())
    if x == -1:
        break
    elif x == 0:
        router_buffer.pop(0)
        now_size -= 1
    else:
        if now_size == buffersize:
            continue
        router_buffer.append(x)
        now_size += 1
    
print(*router_buffer)