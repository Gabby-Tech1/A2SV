def numMagicSquareInside(grid):
    def isMagicSquare(square):
        n = len(square)
        magic_sum = n * (n * n + 1) // 2
        for i in range(n):
            if sum(square[i]) != magic_sum:
                return False
            if sum(square[j][i] for j in range(n)) != magic_sum:
                return False
        if sum(square[i][i] for i in range(n)) != magic_sum:
            return False
        if sum(square[i][n - 1 - i] for i in range(n)) != magic_sum:
            return False
        return True

    count = 0
    rows, cols = len(grid), len(grid[0])
    for i in range(rows - 2):
        for j in range(cols - 2):
            square = [row[j:j + 3] for row in grid[i:i + 3]]
            if isMagicSquare(square):
                count += 1
    return count
    