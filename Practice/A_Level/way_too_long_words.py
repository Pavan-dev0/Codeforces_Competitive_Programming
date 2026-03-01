n=int(input())
for _ in range(n):
    letters=input().strip()

    lens=len(letters)
    if lens<10:
        print(letters)
    else:
        print(letters[0]+str(lens-2)+letters[-1])

