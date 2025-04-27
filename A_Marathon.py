t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    count = 0

    for i in range(len(arr)):
        if arr[0] < arr[i]:
            count += 1
    print(count)
            