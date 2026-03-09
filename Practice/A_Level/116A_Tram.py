n=int(input())

max_capacity=0
current_capacity=0

for _ in range(n):
    a,b=map(int,input().split())
    current_capacity-=a
    current_capacity+=b
    if current_capacity >max_capacity:
        max_capacity=current_capacity

print(max_capacity)