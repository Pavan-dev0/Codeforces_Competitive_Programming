n=int(input())
p=list(map(int,input().split()))

result=[0]*n

for given in range(n):
    recipient=p[given]-1
    result[recipient]=given+1

print(" ".join(map(str,result)))