# take the first input as the total test cases
# take the second input as the total number of size of the board
# take the input of the total candies "as per the size of the board"

from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    board = []
    for _ in range(n):
        row = list(map(int, input().split()))
        board.extend(row)
    
    freq = Counter(board)
    
    # If any color appears more than n*(n-1), it's impossible
    if any(count > n*(n-1) for count in freq.values()):
        print("NO")
    else:
        print("YES")



