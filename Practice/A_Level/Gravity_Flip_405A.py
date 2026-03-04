total_nums=int(input())
n=list(map(int, input().split()))

for i in range(0,total_nums-1):
    for j in range(0,total_nums-1-i):
        if n[j+1]<n[j]:
            n[j+1],n[j]=n[j],n[j+1]
            
print(*n)
            