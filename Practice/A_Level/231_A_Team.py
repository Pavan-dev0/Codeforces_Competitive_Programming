"""
Problem_Name:- Teams Problem
Problem Number:- 231A
Problem difficulty:- Easy

Problem :- Approachtake an integer as input 
no according to that integer loop it and take the inputs now in the inputs if the input of 1 is more that 2 increment count to 1 and so on do the same

"""

ints=int(input())
counts=0
for _ in range(ints):
    a,b,c=map(int,input().split())
    
    if a==1 and b==1 and c==1:
        counts+=1
    elif a==1 and c==1 and b==0:
        counts+=1
    elif b==1 and c==1 and a==0:
        counts+=1
    elif a==1 and b==1 and c==0:
        counts+=1
    else:
        counts+=0

print(counts)    

    