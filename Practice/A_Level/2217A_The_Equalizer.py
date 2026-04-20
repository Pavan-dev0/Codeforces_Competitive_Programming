import sys

def solve():
    # Fast I/O: Reading the four input integers
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = int(input_data[1])
    b = int(input_data[2])
    k = int(input_data[3])

    # Pre-generate Y coordinates. Points are effectively (i, y_coords[i])
    # Because i (the x-coordinate) is already sorted, we save O(N log N) time.
    y_coords = [(a * i + b) % n for i in range(n)]
    
    # s stores the indices of points currently in the set, sorted by x
    s = list(range(n))
    
    # Use bytearray for fast marking and low memory footprint
    removed = bytearray(n)
    results = []
    
    for layer in range(k):
        # A convex hull needs at least 3 points to have an area.
        # If fewer points remain, the area and all subsequent areas are 0.
        if len(s) < 3:
            results.append("0")
            s = [] 
            continue

        # Monotone Chain Algorithm to find Upper and Lower Hulls
        # We include collinear points on the boundary for removal.
        
        # 1. Build Upper Hull
        upper = []
        for i in s:
            yi = y_coords[i]
            while len(upper) >= 2:
                o = upper[-1]
                p = upper[-2]
                # Cross product: (x_o - x_p)(y_i - y_p) - (y_o - y_p)(x_i - x_p)
                # For upper hull, we pop if it makes a "left turn" (cp > 0)
                if (o - p) * (yi - y_coords[p]) - (y_coords[o] - y_coords[p]) * (i - p) > 0:
                    upper.pop()
                else:
                    break
            upper.append(i)
            
        # 2. Build Lower Hull
        lower = []
        for i in s:
            yi = y_coords[i]
            while len(lower) >= 2:
                o = lower[-1]
                p = lower[-2]
                # For lower hull, we pop if it makes a "right turn" (cp < 0)
                if (o - p) * (yi - y_coords[p]) - (y_coords[o] - y_coords[p]) * (i - p) < 0:
                    lower.pop()
                else:
                    break
            lower.append(i)

        # 3. Calculate Doubled Area using the Trapezoid method
        # Doubled Area = |Sum of (x_next - x_curr) * (y_curr + y_next)|
        area2_upper = 0
        for idx in range(len(upper) - 1):
            u1, u2 = upper[idx], upper[idx+1]
            area2_upper += (u2 - u1) * (y_coords[u1] + y_coords[u2])
            
        area2_lower = 0
        for idx in range(len(lower) - 1):
            l1, l2 = lower[idx], lower[idx+1]
            area2_lower += (l2 - l1) * (y_coords[l1] + y_coords[l2])
            
        doubled_area = abs(area2_upper - area2_lower)
        results.append(str(doubled_area))
        
        # 4. Mark all points on the hull boundary for removal
        for i in upper:
            removed[i] = 1
        for i in lower:
            removed[i] = 1
            
        # 5. Filter the set for the next "onion layer"
        # This list comprehension is O(N), totaling O(K*N) across iterations.
        s = [i for i in s if not removed[i]]

    # Print results for all k layers
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()