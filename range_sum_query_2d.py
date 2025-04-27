def __init__(self, matrix: List[List[int]]):
    """
    Initialize the object with a 2D matrix.

    :param matrix: 2D list of integers
    """
    self.matrix = matrix
    self.rows = len(matrix)
    self.cols = len(matrix[0]) if matrix else 0

def sumRegion(row1, col1, row2, col2):
    """
    Calculate the sum of the elements in the rectangle defined by the corners (row1, col1) and (row2, col2).

    :param row1: Starting row index
    :param col1: Starting column index
    :param row2: Ending row index
    :param col2: Ending column index
    :return: Sum of the elements in the specified rectangle
    """
    total = 0
    for i in range(row1, row2 + 1):
        for j in range(col1, col2 + 1):
            total += self.matrix[i][j]
    return total

