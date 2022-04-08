from typing import List

def cut_trees(trees:List, m:int):
    start, end = 0, max(trees)
    while start <= end:
        mid = (start+end)//2
        logs = [t-mid for t in trees if t>mid]
        # 크거나 같다면 높인다 높이를
        if sum(logs) >= m:
            start = mid+1

        else:
            end = mid-1

    return end


N, M = map(int, input().split())
trees = list(map(int,input().split()))

print(cut_trees(trees, M))