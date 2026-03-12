import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line)
    
    line = sys.stdin.readline()
    if not line:
        return
    a = list(map(int, line.split()))

    msb_counts = [0] * 32

    for x in a:
        msb = x.bit_length() - 1
        msb_counts[msb] += 1

    ans = 0
    for count in msb_counts:
        ans += (count * (count - 1)) // 2

    sys.stdout.write(str(ans) + '\n')

line = sys.stdin.readline()
if line:
    t = int(line)
    for _ in range(t):
        solve()
