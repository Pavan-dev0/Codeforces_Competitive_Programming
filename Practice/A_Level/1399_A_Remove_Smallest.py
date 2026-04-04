""" """

ints = int(input())
lists = []
for i in range(ints):
    ts = int(input())
    strs = list(map(int, input().split()))
    lists.append(strs)


for i in range(len(lists)):
    is_small=True
    listss=sorted(lists[i])
    for j in range(len(listss) - 1):
        
        if listss[j+1] - listss[j] > 1:
            is_small=False
            break 
    if is_small:
        print("YES")
    else:
        print("NO")
