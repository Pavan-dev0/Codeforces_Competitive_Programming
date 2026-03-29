import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    
    val = x - 2*y
    
    if val % 3 != 0:
        print("NO")
        continue
    
    k = val // 3
    
    if k < 0:
        print("NO")
        continue
    
    # NEW IMPORTANT CONDITION
    if max(0, -y) <= k // 2:
        print("YES")
    else:
        print("NO")