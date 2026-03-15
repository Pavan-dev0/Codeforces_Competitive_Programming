import sys

def solve():
    n=int(sys.stdin.readline())
    heights=list(map(int ,sys.stdin.readline().split()))

    max_h=max(heights)
    max_i=heights.index(max_h)

    min_h=min(heights)
    min_i=0
    for i in range(n-1,-1,-1):
        if heights[i]==min_h:
            min_i=i
            break

    swaps=max_i+(n-1-min_i)

    if max_i>min_i:
        swaps-=1
    
    print(swaps)

if __name__=='__main__':
    solve()