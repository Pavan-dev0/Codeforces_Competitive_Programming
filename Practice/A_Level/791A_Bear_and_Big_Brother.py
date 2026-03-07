l_weight,b_weight=map(int,input().split())
years_count=0

while l_weight<=b_weight:
    l_weight*=3
    b_weight*=2
    years_count+=1
    
print(years_count)