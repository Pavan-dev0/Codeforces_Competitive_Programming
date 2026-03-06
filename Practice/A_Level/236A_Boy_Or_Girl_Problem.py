n = input()
sets=set()
for i in range(len(n)):
    sets.add(n[i])

if len(sets)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")