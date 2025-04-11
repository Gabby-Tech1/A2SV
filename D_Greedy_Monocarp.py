test_case = int(input())

for _ in range(test_case):
    n, k = map(int, input().split())
    arr_a = list(map(int, input().split()))

    arr_a.sort(reverse=True)

    i = 0
    total = 0
    while i < n:
        if arr_a[i] + arr_a[i+1] < k:
            total += k - arr_a[i+1]
        elif arr_a[i] == k:
            total += 0
        else:
            total += k - arr_a[i]

        i += 1

    print(total)

