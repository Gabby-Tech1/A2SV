test_case = int(input())

for _ in range(test_case):
    number_of_element = int(input())
    array_a = set(map(int, input().split()))
    array_b = set(map(int, input().split()))

    array_c = len(array_a) * len(array_b)
    if array_c > 2:
        print("YES")
    else:
        print("NO")
