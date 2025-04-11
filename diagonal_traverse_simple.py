def findDiagonalOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    
    m, n = len(matrix), len(matrix[0])
    result = []
    
    diagonals = {}
    
    for i in range(m):
        for j in range(n):
            if i + j not in diagonals:
                diagonals[i + j] = []
            diagonals[i + j].append(matrix[i][j])
    
    for d in range(m + n - 1):
        if d % 2 == 0:
            result.extend(reversed(diagonals[d]))
        else:
            result.extend(diagonals[d])
    
    return result
