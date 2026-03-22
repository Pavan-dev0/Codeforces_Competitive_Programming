import sys
input = sys.stdin.readline

def count_ugly(arr):
    mx = 0
    cnt = 0
    for x in arr:
        if x > mx:
            mx = x
            cnt += 1
    return cnt

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    best = p[:]
    min_ugly = count_ugly(p)
    
    for i in range(n):
        p[0], p[i] = p[i], p[0]
        
        cur = count_ugly(p)
        if cur < min_ugly:
            min_ugly = cur
            best = p[:]
        
        p[0], p[i] = p[i], p[0]  # revert
    
    print(*best)