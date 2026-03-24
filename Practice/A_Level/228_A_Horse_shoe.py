"""
Problem Name:- A Horse shoe Problem
Problem Number :- 228_A
Difficulty:- Easy

Approach:- Loop through the total length if the respective index number is not repeated add upto i now you have all the unique datas
after that minus the total length of set value with total length of the input
"""

n=map(int,input().split())
n=list(n)
sets=set()
counts=0
tot_len=len(n)

for i in range(tot_len):
    if n[i] not in sets:
        sets.add(n[i])
        counts+=1
    
print(tot_len-len(sets))

