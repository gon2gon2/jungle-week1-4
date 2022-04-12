# 소요시간 30분

n,w,L = map(int,input().split())
A_ = [*map(int,input().split())]

bridge = []
on_bridge = 0
time = 0
arrive = 0
idx = 0
while arrive != n:
    time += 1
    if bridge and bridge[0][1] == w:
        a = bridge.pop(0)
        arrive += 1
        on_bridge -= a[0]


    if idx < n and on_bridge + A_[idx] <= L:
        bridge.append([A_[idx],0])
        on_bridge += A_[idx]
        idx += 1

    for t in bridge:
        t[1] += 1

print(time)