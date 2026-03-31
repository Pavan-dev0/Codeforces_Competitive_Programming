"""
Problem Number:- 181A
Difficulty:- 
Approach:- 

Understanding:-
Given:- map represented as n*m rectangular table
Robberies are represented as asterisk 
4th Robbery = all four robbed distircts will form vertices of rectangle, parallel to the sides of the map

take input in the format of the map 
and the rows and columns in the format of string
"""

# Codeforces 181A - Series of Crimes

n, m = map(int, input().split())
robberies = []

for i in range(n):
    row = input().strip()
    for j in range(m):
        if row[j] == '*':
            robberies.append((i + 1, j + 1))  # store 1-based

# robberies has 3 points
rows = [r[0] for r in robberies]
cols = [r[1] for r in robberies]

# the missing row is the one not duplicated
for r in rows:
    if rows.count(r) == 1:
        missing_row = r

# the missing col is the one not duplicated
for c in cols:
    if cols.count(c) == 1:
        missing_col = c

print(missing_row, missing_col)
