n=int(input())

if n%2!=0:
    print(-1)

else:
    per=[]
    for i in range(1,n+1,2):
        per.append(i+1)
        per.append(i)
    print(" ".join(map(str,per)))

