def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    if not matrix:
        return

    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

    # Use the first row and first column to mark zeroes
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set zeroes based on marks
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Set the first row to zero if needed
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # Set the first column to zero if needed
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix