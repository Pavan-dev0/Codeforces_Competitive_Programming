num=int(input())
n=map(int,input().split())
nm=list(n)
is_hard=False

for ops in nm:
    if ops==1:
        is_hard=True
        break
if is_hard:
    print("HARD")
else:
    print("EASY")