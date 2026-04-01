nums = int(input())
mxs = []
total = 0
mids = nums // 2

for _ in range(nums):
    sps = list(map(int, input().split()))  # convert to list
    mxs.append(sps)

for i in range(nums):
    for j in range(nums):
        if i == j or i + j == nums - 1 or i == mids or j == mids:
            total += mxs[i][j]

print(total)
