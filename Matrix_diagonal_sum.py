# mat = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]
mat = [[1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]
# mat = [[5]]

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i == j:
            print(mat[i][j], end=" ")
        elif i + j == len(mat) - 1:
            print(mat[i][j], end=" ")