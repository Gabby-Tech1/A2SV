def removeDuplicates(nums):
    """
    This function removes duplicates from a sorted array in-place and returns the new length of the array.
    :param nums: List[int] - A sorted list of integers
    :return: int - The new length of the array after removing duplicates
    """
    if not nums:
        return 0

    # Initialize the index for the next unique element
    unique_index = 1

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the last unique element
        if nums[i] != nums[unique_index - 1]:
            # Update the next unique position with the current element
            nums[unique_index] = nums[i]
            unique_index += 1

    # Return the length of the array with unique elements
    return unique_index