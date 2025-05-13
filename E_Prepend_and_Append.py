t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip() 
    
    left = 0
    right = n - 1
    operations = 0
    
    while left < right:
        if s[left] != s[right]:
            left += 1
            right -= 1
            operations += 1
        else:
            break
    
    remaining_length = n - 2 * operations
    print(remaining_length)