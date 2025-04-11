test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    arr_a = list(map(int, input().split()))

    if n < 3:
        print("NO")

    possible = True
    for i in range(len(arr_a) - 1):
        if arr_a[i] == 1 and arr_a[i-1] == 1:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")

