matrix = [
    [3, 2, 1, 4],
    [6, 7, 11, 9],
    [0, 12, 8, 15],
    [3, -1, 20, -2]
]

rows, cols = len(matrix), len(matrix[0])
prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

for i in range(1, rows+1):
    for j in range(1, cols+1):
        prefix_sum[i][j] = matrix[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]


print(prefix_sum)