def isToeplitsMatrix(matrix):
    if not matrix or not matrix[0]:
        return True
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
                
    return True