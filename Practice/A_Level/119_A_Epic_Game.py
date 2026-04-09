import math

a, b, n = map(int, input().split())

turn = 0  # 0 = Simon, 1 = Antisimon
while True:
    if turn == 0:
        g = math.gcd(a, n)
        if g > n:
            print(1)  # Antisimon wins
            break
        n -= g
    else:
        g = math.gcd(b, n)
        if g > n:
            print(0)  # Simon wins
            break
        n -= g
    turn ^= 1
