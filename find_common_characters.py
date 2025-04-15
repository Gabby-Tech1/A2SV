def commonChars(words):
    """
    Given a list of strings, return a list of characters that are common to all strings.
    
    :param words: List of strings
    :return: List of characters that are common to all strings
    """
    if not words:
        return []

    # Initialize the set with the characters of the first word
    common_set = set(words[0])

    # Iterate through the rest of the words
    for word in words[1:]:
        # Update the common set to keep only characters present in both sets
        common_set.intersection_update(word)

    # Return the sorted list of common characters
    return sorted(common_set)