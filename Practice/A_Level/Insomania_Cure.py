"""
Dragons_Funny_Issue

kth=Punched
lth=tail shut
mth=paws_Trampled
nth=Withdrew Panic
dth=Total_Dragons
inputs:-
k,l,m,n and d
"""
k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())

counts=0
for i in range(1,d+1):
    if i%k==0 or i%l==0 or i%n==0 or i%m==0:
        counts+=1

print(counts) 