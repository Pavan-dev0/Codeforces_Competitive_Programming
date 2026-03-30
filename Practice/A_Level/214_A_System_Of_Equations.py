import math

def count_solutions(n, m):
    count = 0
    for a in range(int(math.sqrt(n)) + 1):
        for b in range(int(math.sqrt(m)) + 1):
            if a*a + b == n and a + b*b == m:
                count += 1
    return count

# Input
n, m = map(int, input().split())
print(count_solutions(n, m))
