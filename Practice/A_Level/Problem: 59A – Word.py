n=input()
upper=sum(1 for i in n if i.isupper())
lower=sum(1 for i in n if i.islower())

if upper>lower:
    print(n.upper())
else:
    print(n.lower())
