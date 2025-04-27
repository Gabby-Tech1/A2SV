# Sample Input

# STDIN       Function
# -----       --------
# 5 3         arr[] size n = 5, queries[] size q = 3
# 1 2 100     queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
# 2 5 100
# 3 4 100

# Sample Output

# 200

def arrayManipulation(n, queries):
    arr = [0] * (n + 1)

    for query in queries:
        a, b, k = query
        arr[a - 1] += k
        arr[b] -= k

    max_value = 0
    current_value = 0

    for i in range(n):
        current_value += arr[i]
        if current_value > max_value:
            max_value = current_value

    return max_value