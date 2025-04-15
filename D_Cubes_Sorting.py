t = int(input())

for _ in range(t):
    n = int(input())
    volumes = list(map(int, input().split()))

    can_be_sorted = False
    
    for i in range(n-1):
        if volumes[i] <= volumes[i+1]:
            can_be_sorted = True
            break
    
    if can_be_sorted:
        print("YES")
    else:
        print("NO")
