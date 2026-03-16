def longest_common_suffix(s1, s2):
    length = 0
    min_len = min(len(s1), len(s2))
    
    for i in range(1, min_len + 1):
        if s1[-i] == s2[-i]:
            length += 1
        else:
            break
            
    return length

str1 = "running"
str2 = "jumping"
print(f"Longest common suffix length: {longest_common_suffix(str1, str2)}")
