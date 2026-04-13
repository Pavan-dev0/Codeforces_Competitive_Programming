"""
Given Problem Description:- There are n stops
has the a(i):- exits
has the b(i):- Entery Point

Trams is empty before arriving at 1st stop 
trams exits so that it becomes empty

Calculate the Minimum Capacity 
"""

n=int(input())
lists=[]
for _ in range(n):
    z,r=map(int,input().split())
    lists.append(z)
    lists.append(r)
res=0
nexts=1
uniq_lists=[]
for i in range(len(lists)-1):
    if i%2==0:
        res+=lists[nexts]
        nexts+=1
        uniq_lists.append(res)
    else:
        res-=lists[nexts]
        nexts+=1
        uniq_lists.append(res)
print(max(uniq_lists))
