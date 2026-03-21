import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def solve():
    t = int(input().strip())
    
    for _ in range(t):
        n, c, k = map(int, input().split())
        a = list(map(int, input().split()))
        
        a.sort()
        
        heap = []
        i = 0
        
        while True:
            # Add all monsters we can currently kill
            while i < n and a[i] <= c:
                heappush(heap, -a[i])
                i += 1
            
            # If none available → stop
            if not heap:
                break
            
            # Take the strongest available monster
            x = -heappop(heap)
            
            # Use flips optimally
            used = min(k, c - x)
            
            # Update power
            c += x + used
            k -= used
        
        print(c)

if __name__ == "__main__":
    solve()