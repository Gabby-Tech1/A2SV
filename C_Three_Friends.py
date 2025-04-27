t = int(input())

for _ in range(t):
    positions = list(map(int, input().split()))
    positions.sort()
    
    a, b, c = positions
    
    # If all three are already at the same position
    if a == b == c:
        total_distance = 0
        
    # If two friends are at the same position
    elif a == b:
        if c - a == 1:  # If the third friend is just one step away
            a += 1
            b += 1
            # c stays the same
            total_distance = 0  # All at same position now
        else:
            a += 1
            b += 1
            c -= 1
            total_distance = abs(a - b) + abs(b - c) + abs(a - c)
    
    elif b == c:
        if b - a == 1:  # If the first friend is just one step away
            # a stays the same
            b -= 1
            c -= 1
            total_distance = 0  # All at same position now
        else:
            a += 1
            b -= 1
            c -= 1
            total_distance = abs(a - b) + abs(b - c) + abs(a - c)
    
    # All three at different positions
    else:
        if a < b:
            a += 1
        
        if c > b:
            c -= 1
        
        if b > a:
            b -= 1
        elif b < c:
            b += 1
            
        total_distance = abs(a - b) + abs(b - c) + abs(a - c)
    
    print(total_distance)