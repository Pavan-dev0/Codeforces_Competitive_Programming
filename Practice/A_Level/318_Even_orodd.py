def even_odds(n, k):
    odd_count = (n + 1) // 2
    if k <= odd_count:
        return 2 * k - 1
    else:
        return 2 * (k - odd_count)

n, k = map(int, input().split())
print(even_odds(n, k))
