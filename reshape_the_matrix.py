def matrixReshape(mat, r, c):
    
    if len(mat) * len(mat[0]) != r * c:
        return mat
    
    flat_list = []
    for row in mat:
        for num in row:
            flat_list.append(num)
            
    reshaped_matrix = []
    for i in range(r):
        reshaped_matrix.append(flat_list[i * c:(i + 1) * c])

    
    return reshaped_matrix