n = int(input())

total_rows = 2 * n + 1

for row in range(total_rows):
    spaces = abs(n - row) * 2
    
    print(" " * spaces, end="")
    
    if row <= n:
        max_num = row
    else:
        max_num = total_rows - row - 1
    
    for num in range(max_num + 1):
        print(num, end="")
        if num < max_num:
            print(" ", end="")
    
    for num in range(max_num - 1, -1, -1):
        print(" " + str(num), end="")
    
    print()