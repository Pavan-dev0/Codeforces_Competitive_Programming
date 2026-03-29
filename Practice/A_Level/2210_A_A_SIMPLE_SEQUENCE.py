def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        # Using the [n-1, n, n-2, ..., 1] pattern
        res = [n-1, n]
        for i in range(n-2, 0, -1):
            res.append(i)
        
        print(*(res))

solve()