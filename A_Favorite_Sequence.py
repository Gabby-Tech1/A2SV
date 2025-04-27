t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    arr = []
    
    left, right = 0, n - 1  

    while left < right:
        arr.append(a[left])
        arr.append(a[right])
        left += 1
        right -= 1
    
    arr.append(a[right]) if left == right else None
        
    print(*arr)