import sys

def solve():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        t = int(line.strip())
    except ValueError:
        return

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        s = list(sys.stdin.readline().strip())
        
        first_1 = -1
        last_1 = -1
        for i in range(n):
            if s[i] == '1':
                if first_1 == -1:
                    first_1 = i
                last_1 = i
        
        if first_1 == -1:
            print(0, 0)
            continue
            
        max_ones = (last_1 - first_1 + 1)
        
        min_ones = 0
        if s.count('1') > 0:
            if s.count('1') == 1:
                min_ones = 1
            else:
                min_ones = 2
        
        print(f"{min_ones} {max_ones}")

if __name__ == '__main__':
    solve()
