C = int(input())

for _ in range(C):
    NS = list(map(int,input().split()[1:]))

    mean = sum(NS)/len(NS)
    over_means = [s for s in NS if s>mean]
    ratio = round(len(over_means)/len(NS)*100,3)
    print(str(ratio).ljust(6,'0')+"%")
