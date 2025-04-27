t = int(input())

for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))
    
    compressed = []
    for height in heights:
        if not compressed or compressed[-1] != height:
            compressed.append(height)
    
    valley_count = 0
    
    if len(compressed) == 1:
        valley_count = 1
    else:
        for i in range(len(compressed)):
            if i == 0 and i + 1 < len(compressed):
                if compressed[i] < compressed[i+1]:
                    valley_count += 1
            elif i == len(compressed) - 1:
                if i - 1 >= 0: 
                    if compressed[i] < compressed[i-1]:
                        valley_count += 1
            elif 0 < i < len(compressed) - 1:
                if compressed[i] < compressed[i-1]:
                    if compressed[i] < compressed[i+1]:
                        valley_count += 1
                
    if valley_count == 1:
        print("YES")
    else:
        print("NO")