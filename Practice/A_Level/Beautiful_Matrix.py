for i in range(1,6):
    row=list(map(int,input().split()))
    for j in range(1,6):
        if row[j-1]==1:
            print(abs(3-i)+abs(3-j))