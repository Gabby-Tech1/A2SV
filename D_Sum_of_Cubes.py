t = int(input())

for _ in range(t):
    x = int(input())
    isFound = False
    
    limit = int(x**(1/3))
    
    left = 1
    right = limit
    
    while left <= right:
        current_sum = left**3 + right**3
        
        if current_sum == x:
            isFound = True
            break
        elif current_sum < x:
            left += 1
        else:
            right -= 1
    
    if isFound:
        print("YES")
    else:
        print("NO")
