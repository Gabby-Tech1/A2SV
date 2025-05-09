def magicSquareInGrid(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # Check for 3x3 magic squares within the grid
    for i in range(rows - 2):
        for j in range(cols - 2):
            # Extract the potential 3x3 magic square
            subgrid = [
                [grid[i][j], grid[i][j+1], grid[i][j+2]],
                [grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2]],
                [grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]
            ]
            
            if isMagicSquare(subgrid):
                count += 1
    
    return count

def isMagicSquare(grid):
    # For a 3x3 magic square, the magic constant is always 15
    magic_constant = 15
    
    # Check if all numbers are distinct and between 1-9
    flat_grid = [grid[i][j] for i in range(3) for j in range(3)]
    if len(set(flat_grid)) != 9 or min(flat_grid) < 1 or max(flat_grid) > 9:
        return False
    
    # Check rows
    for i in range(3):
        if sum(grid[i]) != magic_constant:
            return False
    
    # Check columns
    for j in range(3):
        if sum(grid[i][j] for i in range(3)) != magic_constant:
            return False
    
    # Check diagonals
    if sum(grid[i][i] for i in range(3)) != magic_constant:
        return False
    
    if sum(grid[i][2-i] for i in range(3)) != magic_constant:
        return False
    
    return True