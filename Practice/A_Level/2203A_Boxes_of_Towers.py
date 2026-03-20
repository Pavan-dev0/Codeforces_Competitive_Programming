import math
import sys

def solve():
    line=sys.stdin.readline()
    if not line:
        return 
    t=int(line.strip())


    for _ in range(t):
        n,m,d=map(int,sys.stdin.readline().split())

        max_top=d//m
        max_heig=max_top+1

        ans=math.ceil(n/max_heig)
        print(ans)

if __name__=="__main__":
    solve()