"""
Problem Number:- 112A
Problem Name:- Petya and Strings

Given :- String contains the uppercase and lower letters  
Task:- Compare that in lexicographically 
Letters doesnt matter [uppercase == Lowercase]


"""
input1=input()
input2=input()

for i in range(len(input1)):
    if input1[i].lower() < input2[i].lower():
        print(-1)
        break
    elif input1[i].lower() > input2[i].lower():
        print(1)
        break
else:
    print(0)