import sys

def solve():
    line1 = sys.stdin.readline().strip()
    if not line1:
        return
    n = int(line1)
    s = sys.stdin.readline().strip()

    first_l = s.find('L')

    if first_l == -1:
        print(n)
    else:
        print(first_l + 1)

def main():
    line = sys.stdin.readline().strip()
    if line:
        t = int(line)
        for _ in range(t):
            solve()

if __name__ == "__main__":
    main()