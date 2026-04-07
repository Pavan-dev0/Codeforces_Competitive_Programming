guests=input().strip()
host=input().strip()
pile=input().strip()

if sorted(guests+host)==sorted(pile):
    print("YES")
else:
    print("NO")