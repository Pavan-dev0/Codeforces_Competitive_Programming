import sys

def solve():
    # Read M and N from standard input
    try:
        line = sys.stdin.read().split()
        if not line:
            return
        
        m = int(line[0])
        n = int(line[1])
        
        # Total squares / 2 (integer division)
        result = (m * n) // 2
        
        print(result)
    except EOFError:
        pass

if __name__ == "__main__":
    solve()