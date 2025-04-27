def african_crossword(crossword):
    """
    This function takes a crossword puzzle represented as a list of lists and returns the number of words in the puzzle.
    
    :param crossword: List of lists representing the crossword puzzle
    :return: Number of words in the crossword
    """
    word_count = 0
    
    for row in crossword:
        word_count += sum(1 for cell in row if cell != "")
    
    # Return the total word count
    return word_count

# Example usage:
