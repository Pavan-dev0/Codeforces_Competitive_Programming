n=int(input())
strs=list(map(int,input().split()))
counts=0
comps=strs[0]
mps=strs[0]
for i in range(1,len(strs)):
    if strs[i]>comps:
        counts+=1
        comps=strs[i]
    elif strs[i]<mps:
        counts+=1
        mps=strs[i]

print(counts)