import sys

def solve():

    t=int(sys.stdin.readline())
    for _ in range(t):
        n=int(sys.stdin.readline())
        
        a=list(map(int , sys.stdin.readline().split()))

        if sum(a)%2==0:
            print("YES")
        
        else:
            print("NO")

if __name__=='__main__':
    solve()