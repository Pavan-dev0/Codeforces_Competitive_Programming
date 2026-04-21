def count_pairs(n, d, arr):
    arr.sort()
    count = 0
    r = 0

    for l in range(n):
        while r < n and arr[r] - arr[l] <= d:
            r += 1
        
        valid = r - l - 1
        count += valid

    return count * 2


# INPUT
n, d = map(int, input().split())
arr = list(map(int, input().split()))

# OUTPUT
print(count_pairs(n, d, arr))