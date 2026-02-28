"""
Codeforces 339A - Helpful Maths
Level: A
Concept: String manipulation, Sorting
"""

n=input()
nums=n.split('+')
nums.sort()
print('+'.join(nums))