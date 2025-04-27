t = int(input())

for _ in range(t):
    n = int(input())
    elements = list(map(int, input().split()))

    isChecked = True
    counts = [0] * (max(elements)+1)

    for i in elements:
        counts[i] += 1

    for i in range(1, len(counts)):
        if counts[i] > counts[i-1]:
            isChecked = False

    if isChecked:
        print("YES")
    else:
        print("NO")
