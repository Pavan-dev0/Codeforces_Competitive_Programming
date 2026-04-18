import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    c = []
    m = []
    
    for _ in range(n):
        ci, pi = map(int, input().split())
        c.append(ci)
        m.append(1 - pi / 100)
    
    dp = 0.0
    
    for i in range(n - 1, -1, -1):
        dp = max(dp, c[i] + m[i] * dp)
    
    print(f"{dp:.10f}")