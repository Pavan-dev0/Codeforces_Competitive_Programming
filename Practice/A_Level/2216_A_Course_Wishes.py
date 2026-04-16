t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt = [0] * (k + 2)
    for x in b:
        cnt[x] += 1

    ops = []

    while True:
        done = True
        for i in range(n):
            if b[i] <= k:
                done = False
                nxt = b[i] + 1

                if nxt == k + 1 or cnt[nxt] < a[nxt]:
                    # perform operation
                    cnt[b[i]] -= 1
                    b[i] += 1
                    cnt[b[i]] += 1
                    ops.append(i + 1)
                    break
        if done:
            break
        else:
            # check if no operation happened in this round
            if len(ops) > 1000:
                break

    if any(x <= k for x in b):
        print(-1)
    else:
        print(len(ops))
        print(*ops)