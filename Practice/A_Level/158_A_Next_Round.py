n, k = map(int, input().split())
x=list(map(int,input().split()))

th=x[k-1]
count=sum(1 for s in x if s>0 and s>=th)
print(count)
