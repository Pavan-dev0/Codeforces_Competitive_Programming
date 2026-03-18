def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        
        blocks = 0
        max_block = 0
        i = 0
        while i < n:
            if s[i] == '1':
                length = 0
                while i < n and s[i] == '1':   # FIXED: check '1' not 'l'
                    length += 1
                    i += 1
                blocks += 1
                max_block = max(max_block, length)
            else:
                i += 1
        
        print(blocks, max_block)
