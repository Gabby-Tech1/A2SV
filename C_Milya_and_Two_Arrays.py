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

# def distinct_array(test_case, array_a, array_b):
#     for _ in range(test_case):

#         array_c = len(set(array_a)) * len(set(array_b))
#         if array_c > 2:
#             return "YES"
#         else:
#             return "NO"
        
# results = distinct_array(5, [1, 2, 1, 2], [1, 2, 1, 2])
# print(results)