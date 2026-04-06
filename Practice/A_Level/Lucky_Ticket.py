"""
Problem_Number:- 146_A
Problem_difficulty:- Easy

Approach:-  Lucky_Numbers==> Positive Numbers, Decimal Records only contains the lucky digits 4 and 7
Example:- 47,744,4 lucky and 5,17,467 Arent Lucky Numbers


"""
def is_lucky_ticket(n, ticket):
    # Condition 1: All digits must be 4 or 7
    if any(ch not in '47' for ch in ticket):
        return "NO"
    
    # Split into two halves
    half = n // 2
    first_half = ticket[:half]
    second_half = ticket[half:]
    
    # Condition 2: Sum of halves must match
    if sum(map(int, first_half)) == sum(map(int, second_half)):
        return "YES"
    else:
        return "NO"


# Example usage:
n = int(input().strip())
ticket = input().strip()
print(is_lucky_ticket(n, ticket))
