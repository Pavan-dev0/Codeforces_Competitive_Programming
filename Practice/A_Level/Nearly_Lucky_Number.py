s = input().strip()
count = 0

for char in s:
    if char == '4' or char == '7':
        count += 1

if count == 4 or count == 7:
    print("YES")
else:
    print("NO")