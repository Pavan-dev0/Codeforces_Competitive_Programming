import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        p, q = map(int, sys.stdin.readline().split())
        
        k = 3 * p - 2 * q
        # Bob wins if k >= 0 and q - k >= 1
        if k >= 0 and q - k >= 1:
            print("Bob")
        else:
            print("Alice")

if __name__ == "__main__":
    solve()
